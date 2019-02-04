import json
import codecs
import pandas as pd
import xang_pytextrank as pyt

path=r'D:\sample-S2-records'


a=[]
with codecs.open("wordlist.csv", 'r','utf-8') as f:
    for line in f.readlines():
        a.append(json.loads(line)['paperAbstract'])

## Remove blank abstracts
a = list(filter(None, a))
t = [pyt.top_keywords_sentences(a[i])[1] for i in range(len(a))]

data=pd.DataFrame({'Abstract':a,'Keywords':t})
data.to_csv('TextRank.csv',index=False)