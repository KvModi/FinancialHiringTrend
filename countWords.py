import csv
text = open('wordlist.csv').read()
words = text.split(',')
word_count = {}
for word in words:
    word=word.lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count
topHundred={}
word_count_list = sorted(word_count, key=word_count.get, reverse=True)
updatedword={}
for word in word_count_list[:100]:
    updatedword.update({word:word_count[word]})

updatedword2=[]
updatedword2=list(updatedword)
print ("dd",updatedword2)


with open("topcount2.csv", "w+") as f:
    writer = csv.writer(f)

    writer.writerow(updatedword2)


print("dict",word_count_list[:100])
with open("topcount.csv", "w+") as f:
    writer = csv.writer(f)
    writer.writerow(updatedword)
    writer.writerow(updatedword.values())


