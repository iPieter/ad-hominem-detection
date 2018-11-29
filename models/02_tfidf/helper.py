from nltk.util import skipgrams
import pandas as pd

def get_data():
    return pd.read_csv('../../data/merged_datasets.csv', usecols=(['body', 'isAdHominem']))

def get_data_with_skip_n_grams(n, k):
    data = get_data()
    for index, row in data.iterrows():
        data.at[index, 'body'] = list(skipgrams(data.loc[index, 'body'].split(), n, k))
    return data