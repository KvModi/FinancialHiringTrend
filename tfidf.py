import numpy as np
import csv
from sklearn.feature_extraction.text import TfidfVectorizer

csvfile=open('wordlist.csv','r')
corpus=open('wordlist.csv','r')

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

feature_array=np.array(vectorizer.get_feature_names())
tfidf_sorting=np.argsort(X.toarray()).flatten()[::-1]
n=100
top_n=feature_array[tfidf_sorting][:n]
print(top_n)
with open("ifcount.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(top_n)

