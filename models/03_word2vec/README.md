# Model01.h5

- 200 features
- removed stopwords
- TF-IDF multiplication

```
model.add(LSTM(300, input_shape=(features, len(wv_from_bin["test"]))))
model.add(Dense(1))
```

# Model02.h5

- 200 features
- removed stopwords
- TF-IDF multiplication
- Treshold at 0.095

```
model.add(Dense(32, input_shape=(features, len(wv_from_bin["test"]))))
model.add(Flatten())
model.add(Dense(1))
```

# Model03.h5

- Word2vec on sentence level
- Gensim vectorizer
- In total, the train contains 279 ad hominems
- In total, the test contains 121 ad hominems


```
model = Sequential()
model.add(Masking(mask_value=0., input_shape=(maxLength, 300)))
model.add(Bidirectional(GRU(10, return_sequences=True), merge_mode='concat'))
model.add(Bidirectional(GRU(10), merge_mode='concat'))
model.add(Dense(64))
model.add(Dense(1))
```