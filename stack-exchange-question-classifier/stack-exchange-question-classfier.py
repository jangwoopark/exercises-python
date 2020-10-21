import json
import re
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier

count = 0
topic = []
textarray = []

with open('training.json') as f:
    for line in f:
        count += 1
        if count == 1: continue
        post = json.loads(line)
        topic.append(post['topic'])
        sen = post['question'] + " " + post['excerpt']
        textarray.append(sen)

X_train = np.array(textarray)
y_train = topic

txtcfl = Pipeline([('vect',CountVectorizer()),
                  ('tfidf',TfidfTransformer()),
                  ('clf',LinearSVC())])

txtcfl.fit(X_train, y_train)

testarray = []

for i in range(int(input())):
    j = json.loads(input())
    sen = j['question'] + " " + j['excerpt']
    testarray.append(sen)

predicted = txtcfl.predict(testarray)

for i in predicted:
    print(i)
