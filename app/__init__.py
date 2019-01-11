import os
from flask import Flask, request, abort, Response, jsonify
from flask_cors import CORS
import pandas as pd
import tensorflow as tf
import keras
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import nltk
import gensim
from gensim.models import KeyedVectors
from gensim.utils import simple_preprocess
from gensim.test.utils import datapath
from keras.models import load_model
from keras.layers import Input, Embedding, GRU, Dense, Masking, Bidirectional, concatenate, Dropout,Flatten
from keras.models import Model
import sqlite3

conn = sqlite3.connect("log.db", check_same_thread=False)

c = conn.cursor()

app = Flask(__name__)
CORS(app)

maxLength = 400
docVectorLength = 500  

docModel = gensim.models.doc2vec.Doc2Vec.load("models/03_doc2vec/reddit-doc2vec.model") 

def combineData( dataset ):
    #dataset["length"] = dataset["body"].apply( lambda x: len(word_tokenize(x)))
    #maxLength = dataset["length"].max()    
    paragraphRepresentations = np.zeros((1, maxLength, 300))
    docVectors = np.zeros((1, docVectorLength))
    tags = np.zeros((1, maxLength, len(pos_tags_list)))
    
    paragraph = dataset
    i = 0
    # Split the sentence into an array of (cleaned) words
    splittedSentence = simple_preprocess(paragraph, deacc=True)
    if len(splittedSentence) > 400:
        splittedSentence = splittedSentence[0:400]
    if len(splittedSentence) != 0:
        for index, tag in enumerate(X_int.transform(np.array(nltk.pos_tag(splittedSentence))[:,1])):
            tags[i, index, tag] = 1.
    # Generate docVector first
    docVectors[i] = docModel.infer_vector(splittedSentence)
    
    # Enumerate over the words in the tags-array (col 0 = words, col 1 = POS tags)
    for j, word in enumerate(splittedSentence):
        #print("{}: {} ({})".format(i, j, word))
        if word.lower() in wv_from_bin:
            paragraphRepresentations[i, j] = wv_from_bin[word.lower()] 
    return paragraphRepresentations, docVectors, tags

def create_model():  
    word2vecInput = Input(shape=(maxLength, 300), name='word2vec')
    doc2vecInput = Input(shape=(docVectorLength,), name='doc2vec')
    posTagsInput = Input(shape=(maxLength, len(pos_tags_list)), name='pos_tags')

    # Network for word vectors
    x = Masking(mask_value=0., input_shape=(maxLength, 300))(word2vecInput)
    #x = Bidirectional(GRU(100, return_sequences=True), merge_mode='ave')(x) 
    wordout = Bidirectional(GRU(100, activation="relu"), merge_mode='ave')(x)

    # Add another network for the pos tags
    x = Masking(mask_value=0., input_shape=(maxLength, len(pos_tags_list)))(posTagsInput)
    posout = Bidirectional(GRU(100, activation="relu"), merge_mode='ave')(x)

    # Add word vectors and doc vectors together
    x = concatenate([wordout, doc2vecInput, posout])
    x = Dense(64, activation="relu")(x)
    x = Dropout(0.1)(x)
    x = Dense(64, activation="relu")(x)
    x = Dropout(0.1)(x)
    output = Dense(2, activation="sigmoid", name="output")(x)

    model = Model(inputs=[word2vecInput, doc2vecInput, posTagsInput], outputs=[output])

    model.compile(optimizer='adadelta',
                loss='binary_crossentropy',
                metrics=['binary_accuracy'])

    return model

global graph
nltk.download('tagsets')

wv_from_bin = KeyedVectors.load_word2vec_format(datapath("/Users/pieterdelobelle/Downloads/GoogleNews-vectors-negative300-SLIM.bin.gz"), binary=True)  # C binary format

pos_tags_list = np.array(['CC', 'CD', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS','NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB', 'DT', "''"] )
X_int = LabelEncoder().fit(pos_tags_list.reshape(-1, 1))
graph = tf.get_default_graph()
model = create_model()
#model.load_weights('models/03_doc2vec/model08.h5')
model.load_weights('models/03_doc2vec/model_crazyMizedNN-200words.h5')

@app.route('/predict', methods=["POST"])
def predict():
    par = request.form["par"]
    print("Requested analysis of {}. ".format(par))
    print( par.__class__)
    c.execute("INSERT INTO request (par) VALUES(?)", [par])
    conn.commit()

    x1, x2, x3 = combineData(par)
    with graph.as_default():
        result = model.predict({'word2vec': x1, 'doc2vec': x2, 'pos_tags': x3})
        print( result )
        return json.dumps(result.tolist())

@app.route('/learn', methods=["POST"])
def learn():
    par = request.form["par"]
    label = float(request.form["label"])
    print("Label {} for '{}'. ".format(label, par))

    c.execute(
        "INSERT INTO learn (par, label) VALUES(?,?)",
        (par, label))

    conn.commit()

    print(np.array([[1-label, label]]).T)
    print(np.array([[1-label, label]]).T.shape)
    x1, x2, x3 = combineData(par)
    with graph.as_default():
        result = model.train_on_batch({'word2vec': x1, 'doc2vec': x2, 'pos_tags': x3}, {"output": np.array([[1-label, label]])})
        print( result )
        print( result.__class__ )
        return json.dumps(result[0].astype(float))