from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO as StringIO
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from nltk import word_tokenize
from nltk import pos_tag
import string
import os
script_dir = os.path.dirname(os.path.abspath(_file_)) #<-- absolute dir the script is in
rel_path = "/Users/erin/Desktop/PDF/1234merge.pdf"
abs_file_path = os.path.join(script_dir, rel_path)
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    fp = open(abs_file_path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

a = convert_pdf_to_txt('result.pdf')
print(a)


import re
List = re.sub("[^\w*$]", " ",  a)
#print(List)
words = re.sub("\d+", "", List).split()
print("after split: ", words)

# nltk.download('averaged_perceptron_tagger')
POS_tag = pos_tag(words)


print("Tokenized Text with POS tags: \n")
print (POS_tag)

from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

adjective_tags = ['JJ', 'JJR', 'JJS']

lemmatized_text = []

for word in POS_tag:
    if word[1] in adjective_tags:
        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0], pos="a")))
    else:
        lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0])))  # default POS = noun

print("Text tokens after lemmatization of adjectives and nouns: \n")
print(lemmatized_text)

POS_tag = pos_tag(lemmatized_text)

print ("Lemmatized text with POS tags: \n")
print (POS_tag)

stopwords = []

wanted_POS = ['NN','NNS','NNP','NNPS','JJ','JJR','JJS','VBG','FW']

for word in POS_tag:
    if word[1] not in wanted_POS:
        stopwords.append(word[0])

punctuations = list(str(string.punctuation))

stopwords = stopwords + punctuations
rel_stopword_path="long_stopwords.txt"
stopword_path=os.path.join(script_dir, rel_stopword_path)
stopword_file = open(stopword_path, "rb")
#Source = https://www.ranks.nl/stopwords

lots_of_stopwords = []

for line in stopword_file.readlines():
    lots_of_stopwords.append(str(line.strip()))

stopwords_plus = []
stopwords_plus = stopwords + lots_of_stopwords
stopwords_plus = set(stopwords_plus)

#Stopwords_plus contain total set of all stopwords
processed_text = []
for word in lemmatized_text:
    if word not in stopwords_plus:
        processed_text.append(word)

print ("Processed text: ",processed_text)

with open('processed_text.txt', 'w') as f:
    for item in processed_text:
        f.write("%s\n" % item)
#new_file.close()
print("Hello")

text = processed_text



vocabulary = list(set(processed_text))
print (vocabulary)

import numpy as np
import math

vocab_len = len(vocabulary)

weighted_edge = np.zeros((vocab_len, vocab_len), dtype=np.float32)

score = np.zeros((vocab_len), dtype=np.float32)
window_size = 3
covered_coocurrences = []

for i in xrange(0, vocab_len):
    score[i] = 1
    for j in xrange(0, vocab_len):
        if j == i:
            weighted_edge[i][j] = 0
        else:
            for window_start in xrange(0, (len(processed_text) - window_size)):

                window_end = window_start + window_size

                window = processed_text[window_start:window_end]

                if (vocabulary[i] in window) and (vocabulary[j] in window):

                    index_of_i = window_start + window.index(vocabulary[i])
                    index_of_j = window_start + window.index(vocabulary[j])

                    # index_of_x is the absolute position of the xth term in the window
                    # (counting from 0)
                    # in the processed_text

                    if [index_of_i, index_of_j] not in covered_coocurrences and math.fabs(index_of_i - index_of_j) != 0:
                        weighted_edge[i][j] += 1 / math.fabs(index_of_i - index_of_j)
                        covered_coocurrences.append([index_of_i, index_of_j])

                        inout = np.zeros((vocab_len), dtype=np.float32)

                        for i in xrange(0, vocab_len):
                            for j in xrange(0, vocab_len):
                                inout[i] += weighted_edge[i][j]

MAX_ITERATIONS = 50
d = 0.85
threshold = 0.0001  # convergence threshold

for iter in xrange(0, MAX_ITERATIONS):
    prev_score = np.copy(score)

    for i in xrange(0, vocab_len):

        summation = 0
        for j in xrange(0, vocab_len):
            if weighted_edge[i][j] != 0:
                summation += (weighted_edge[i][j] / inout[j]) * score[j]

        score[i] = (1 - d) + d * (summation)

    if np.sum(np.fabs(prev_score - score)) <= threshold:  # convergence condition
        print ("Converging at iteration " + str(iter) + "....")
        break

        for i in xrange(0, vocab_len):
            print ("Score of " + vocabulary[i] + ": " + str(score[i]))

            phrases = []

            phrase = " "
            for word in lemmatized_text:

                if word in stopwords_plus:
                    if phrase != " ":
                        phrases.append(str(phrase).strip().split())
                    phrase = " "
                elif word not in stopwords_plus:
                    phrase += str(word)
                    phrase += " "

            print ("Partitioned Phrases (Candidate Keyphrases): \n")
            print (phrases)


unique_phrases = []

for phrase in phrases:
    if phrase not in unique_phrases:
        unique_phrases.append(phrase)

print ("Unique Phrases (Candidate Keyphrases): \n")
print (unique_phrases)

for word in vocabulary:
    # print word
    for phrase in unique_phrases:
        if (word in phrase) and ([word] in unique_phrases) and (len(phrase) > 1):
            # if len(phrase)>1 then the current phrase is multi-worded.
            # if the word in vocabulary is present in unique_phrases as a single-word-phrase
            # and at the same time present as a word within a multi-worded phrase,
            # then I will remove the single-word-phrase from the list.
            unique_phrases.remove([word])

print ("Thinned Unique Phrases (Candidate Keyphrases): \n")
print (unique_phrases)

phrase_scores = []
keywords = []
for phrase in unique_phrases:
    phrase_score=0
    keyword = ''
    for word in phrase:
        keyword += str(word)
        keyword += " "
        phrase_score+=score[vocabulary.index(word)]
    phrase_scores.append(phrase_score)
    keywords.append(keyword.strip())

i=0
for keyword in keywords:
    print ("Keyword: '"+str(keyword)+"', Score: "+str(phrase_scores[i]))
    i+=1

    sorted_index = np.flip(np.argsort(phrase_scores), 0)

    keywords_num = 10

    print ("Keywords:\n")

    for i in xrange(0, keywords_num):
        print (str(keywords[sorted_index[i]]) + ", ",)