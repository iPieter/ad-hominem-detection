import gensim
import pandas as pd

def tokenizeIt(arr):
    """Tokenize for the first column of an array of strings. Returns the same array tokenized."""
    for i, line in arr.iterrows():
        yield " ".join(list(gensim.utils.simple_preprocess(str(line[0]))))

def preprocess_df(df):
    """Remove stop words and special characters, sets lowercase, etc. on the first row of a data frame.
    Returns the same data frame with the modified first row."""
    cols = list(df)
    tokenized = list(tokenizeIt(df))
    df[cols[0]] = tokenized
    return df