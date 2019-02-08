# /Users/krishnamodi/PycharmProjects/projectOne/
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import string
import os

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "result.pdf"
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
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue().lower()

    fp.close()
    device.close()
    retstr.close()
    return text


a = convert_pdf_to_txt('result.pdf')


"""
with open("topcount2.csv", "w+") as f:
    writer = csv.writer(f)

    writer.writerow(updatedword2)

"""
import re

List = re.sub("[^\w*$]", " ", a)
# print(List)
words = re.sub("\d+", "", List).split()
print("after split: ", words)

with open('resultText.txt', 'w+') as f:
    for item in words:
        item=item.lower()
        f.write("%s\n" % item)

# nltk.download('averaged_perceptron_tagger')
POS_tag = pos_tag(words)

print("Tokenized Text with POS tags: \n")
print(POS_tag)

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

print("Lemmatized text with POS tags: \n")
print(POS_tag)

stopwords = []

wanted_POS = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VBG', 'FW']

for word in POS_tag:
    if word[1] not in wanted_POS:
        stopwords.append(word[0])

punctuations = list(str(string.punctuation))

stopwords = stopwords + punctuations
rel_stopword_path = "long_stopwords.txt"
stopword_path = os.path.join(script_dir, rel_stopword_path)
stopword_file = open(stopword_path, "rb")
# Source = https://www.ranks.nl/stopwords

lots_of_stopwords = []

for line in stopword_file.readlines():
    lots_of_stopwords.append(str(line.strip()))

stopwords_plus = []
stopwords_plus = stopwords + lots_of_stopwords
stopwords_plus = set(stopwords_plus)

#Stopwords_plus contain total set of all stopwords
processed_text = []
i=1;
for word in lemmatized_text:
    if word not in stopwords_plus:
       # processed_text = processed_text.lower()
        processed_text.append(word)
        i=i+1



print("Processed text: ", processed_text)

with open('processed_text.txt', 'w+') as f:
    for item in processed_text:
        item=item.lower()
        f.write("%s\n" % item)
# new_file.close()
print(i)