import gensim
import pandas as pd
import numpy as np

def read_corpus(data_frame, tokens_only=False):
    """In data frame, first column should be the text input. Output is the preprocessed data. Tags will be the index of the data frame."""
    for i, line in data_frame.iterrows():
        if tokens_only:
            yield gensim.utils.simple_preprocess(str(line[0]))
        else:
            # For training data, add tags
            yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(str(line[0])), [i])

def ggdoc2vec_train(train_data, epochs = 10, vec_size = 100, min_count = 10):
    """Train data is a data frame. First column is expected to be the text input to be vectorized. Output is the doc2vec model"""
    train_corpus = list(read_corpus(train_data))                                       # Preprocessing
    model = gensim.models.doc2vec.Doc2Vec(vector_size=vec_size, min_count=min_count, epochs=epochs)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)  # Training
    return model

def ggdoc2vec_infer(model_filepath, test_data):
    """Test data is a data frame. First column are the text input and second are the labels. model_filepath is the file location for the doc2vec model.
    Output is the same data frame, but instead of text for the body, we have a vector."""
    trained_model = gensim.models.doc2vec.Doc2Vec.load(model_filepath)                                                # Load trained model
    cols = list(test_data)                                                             # Get column names
    test_corpus = list(read_corpus(test_data, tokens_only=True))                       # Preprocessing
    vectorized_bodies = []
    for body in test_corpus:
        vectorized_bodies.append(trained_model.infer_vector(body))
    test_data[cols[0]] = vectorized_bodies
    return test_data