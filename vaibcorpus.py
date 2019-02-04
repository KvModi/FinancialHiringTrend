from sklearn.feature_extraction.text import TfidfVectorizer
import csv

csvfile = open('wordlist.csv', 'r')
#words = csvfile.split(',')
corpus = open('wordlist.csv', 'r')
print(corpus)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
#['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
print(X,"-")
