import csv
import json

csvfile = open('wordlist.csv', 'r')
jsonfile = open('fileword.json', 'w')

fieldnames = ("Word","Frequency")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')