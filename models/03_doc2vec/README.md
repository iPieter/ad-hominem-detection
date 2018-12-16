# Model05.h5

- Word2vec
- Doc2vec
- Only 3k paragraphs

```
word2vecInput = Input(shape=(maxLength, 300), name='word2vec')
doc2vecInput = Input(shape=(docVectorLength,), name='doc2vec')

# Network for word vectors
x = Masking(mask_value=0., input_shape=(maxLength, 300))(word2vecInput)
#x = Bidirectional(GRU(100, return_sequences=True), merge_mode='ave')(x) 
wordout = Bidirectional(GRU(100), merge_mode='ave')(x)

# Add word vectors and doc vectors together
x = concatenate([wordout, doc2vecInput])
x = Dense(64)(x)
x = Dropout(0.1)(x)
x = Dense(64)(x)
x = Dropout(0.1)(x)
output = Dense(2, activation="sigmoid", name="output")(x)

model = Model(inputs=[word2vecInput, doc2vecInput], outputs=[output])
```
