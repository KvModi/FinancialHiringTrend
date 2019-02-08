import textrank
import os
import requests
import re
from summa import keywords
import pandas as pd
import string
script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "venv/processed_text.txt"
result_path="textRankList.csv"
abs_file_path = os.path.join(script_dir, rel_path)
result_file_path= os.path.join(script_dir, result_path)
text = open(abs_file_path, 'r',  encoding='utf-8').read()
textProcess = text.split()
textProcess = ' '.join(textProcess)
#print(partialclean)
#cleantext = partialclean.lower()
# printable = set(string.printable)
# text = list(filter(lambda x: x in printable, text)) #filter funny characters, if any.
# text = [' '.join(e for e in text if e.isalnum())]
processed_text = re.sub('\W+', ' ', textProcess)

punctuations = list(str(string.punctuation))
stopwords = []
stopwords = stopwords + punctuations
rel_stopword_path = "long_stopwords.txt"
stopword_path = os.path.join(script_dir, rel_stopword_path)
stopword_file = open(stopword_path, "rb")
# Source = https://www.ranks.nl/stopwords



keywords = keywords.keywords(processed_text, ratio=0.2, words=None, language="english", split=False, scores=False,
                             deaccent=False, additional_stopwords=stopword_file)
keywordlist = keywords.split('\n')
dataframeword = pd.DataFrame({'keyWords': keywordlist})
keywordsTxtRank_DescOrderCSV = dataframeword.to_csv(result_file_path,index=None)