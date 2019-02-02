import csv
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "venv/processed_text.txt"
abs_file_path = os.path.join(script_dir, rel_path)

processedfile= open(abs_file_path, "rb")
#processed_text = fileOpen.readlines()

processed_text = []

for line in processedfile.readlines():
    line=line.decode("utf-8")
    processed_text.append((line.strip()))
    print(str(line.strip()))


print(processed_text)
#with open('wordlist.csv', 'w+', newline='') as myfile:
 #   wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  #  wr.writerow(processed_text)

with open('wordlist.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(processed_text)
