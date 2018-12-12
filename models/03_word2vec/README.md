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