
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from gensim.test.utils import datapath
from gensim.models import KeyedVectors
from sklearn.metrics import confusion_matrix
import itertools
from sklearn.model_selection import train_test_split
import sys

if (len(sys.argv) != 3):
    print("Usage: script.py <full path to w2v> <path to dataset>")

print("importing word2vec")
wv_from_bin = KeyedVectors.load_word2vec_format(datapath(sys.argv[1]), binary=True)  # C binary format
print("imported word2vec")

df = pd.read_csv(sys.argv[2], sep=",", index_col=0, header=0, names=["body", "isAdHominem"])

train, test = train_test_split( df, test_size=0.3, random_state=3)

print("In total, the train contains", sum(train["isAdHominem"] == True), "ad hominems")
print("In total, the test contains", sum(test["isAdHominem"] == True), "ad hominems")


# In[9]:


features=3000


# In[10]:


print("Starting TF-IDF vectorizer")
from sklearn.feature_extraction.text import TfidfVectorizer
v = TfidfVectorizer( ngram_range = (1, 1), max_features=features, stop_words="english")
v.fit(train['body'].values.astype('U'))
x_train = v.transform(train['body'].values.astype('U'))
x_test = v.transform(test['body'].values.astype('U'))


# In[9]:



def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
        
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def combineData( dataset ):
    train_w2v = np.zeros( (dataset.shape[0], len(v.vocabulary_), len(wv_from_bin["test"])))
    for i in range(0,dataset.shape[0]):
        if (100* i / dataset.shape[0] % 10 == 0):
            print("{} of {} ({} %)\r".format(i, dataset.shape[0], 100* i / dataset.shape[0]))
    
        train_w2v[i] = np.multiply(wordvecs.T,x_train[i,:].toarray().flatten()).T
    return train_w2v


df.head()



test_x = combineData(x_train)


# In[12]:



test_y = combineData(x_test)



# In[ ]:


print("fitting classifier")
from sklearn.svm import LinearSVC
clf = LinearSVC().fit(test_x.reshape(test_x.shape[0],-1), train["isAdHominem"])
print("finished fitting " + LinearSVC.__name__ )


# In[ ]:


predicted = clf.predict(test_y.reshape(test_y.shape[0],-1))


# In[ ]:


# Compute confusion matrix
cnf_matrix = confusion_matrix(test["isAdHominem"], predicted)

np.set_printoptions(precision=2)

title="Confusion matrix for " + LinearSVC.__name__

# Plot normalized confusion matrix
fig = plt.figure()
plot_confusion_matrix(cnf_matrix, classes=["no ad hominem", "ad hominem"],normalize=False, 
                      title=title)

print('plots exported.png')
fig.savefig("plt_not_normalized.png")

# Plot non-normalized confusion matrix
fig = plt.figure()
plot_confusion_matrix(cnf_matrix, classes=["no ad hominem", "ad hominem"],normalize=True, 
                      title=title)
fig.savefig("plt_normalized.png")

