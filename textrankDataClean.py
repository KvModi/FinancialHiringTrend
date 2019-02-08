import os

import csv
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path1 = "textrankdata2.txt"
abs_file_path1 = os.path.join(script_dir, rel_path1)

rel_path2 = "processed_text.txt"
abs_file_path2 = os.path.join(script_dir, rel_path2)



processedfile1= open(abs_file_path1, "rb")
processedfile2= open(abs_file_path2, "rb")
#processed_text = fileOpen.readlines()

processed_text1 = []

processed_text2 = []

for line in processedfile1.readlines():
    line=line.decode("utf-8")
    processed_text1.append((line.strip()))
    #print(str(line.strip()))

for line in processedfile2.readlines():
    line=line.decode("utf-8")
    processed_text2.append((line.strip()))
    #print(str(line.strip()))

processed_text12 = []
processed_text22 = []

print(len(processed_text1))
print(len(processed_text2))

for i in processed_text1:
  if i not in processed_text12:
    processed_text12.append(i)

for i in processed_text2:
  if i not in processed_text22:
    processed_text22.append(i)

print("textrank",len(processed_text12))
print("processed",len(processed_text22))

import networkx as nx

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)


with open('textranklist.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    for i in range(100):
        wr.writerow(processed_text12[i][1])
        print("textrank", len(processed_text12))
        print("processed", len(processed_text22))


