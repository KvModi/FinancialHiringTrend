import csv
import pandas as pd
import numpy as np
import re
import dask

str1="ClustersList.csv" # List of different clusters with cluster name as headers
str2="LemmatisedData.csv" # List of all the jobs from all the 12 teams
def loading(str):
    return  pd.read_csv(str)
def JobClassification(str1,str2):

    df = pd.read_csv(str1) # read the list of clusters
    labels = list(df.columns.values) # reading the headers of clusters
    print (labels)
    size = len(labels) #size is the keywords in cluster
    print (size)
    with open(str2,'r') as data: #Reading the lemmatised data
        reader2 = csv.reader(data)
        column = [row[4]for row in reader2] #from job description column


        Y = np.array(column) # converting job description data into array
        print (Y[0],"of",Y.size,"jobs")

        with open(str2, 'r') as data: # reading the lematized list
            reader2 = csv.reader(data)
            column_bank = [row[3] for row in reader2] # bank name
            Z = np.array(column_bank)
            print (Z[0])
        with open(str2, 'r') as data:
            reader2 = csv.reader(data)
            column_jobTitle = [row[5] for row in reader2] #job title
            A = np.array(column_jobTitle)
            print (A[0])
        path = "result.csv"
    with open(path,'w') as f:
        csv_write = csv.writer(f)
        csv_head = ["Job_ID","Bank_Name","Job_Title","Cluster_Name","The_amount_of_word_count"]
        csv_write.writerow(csv_head)
    for num2 in range(1, (Y.size - 1)):  # for each job description
        comp = 0
        for num3 in range(0, size):#for every cluster
            with open(str1,'r') as cluster:
                reader1 = csv.reader(cluster)
                column1 = [row[num3]for row in reader1]
                X = np.array(column1)
                X1 = X.tolist()
                while '' in X1:
                    X1.remove('')
                X = np.array(X1)
                count=0
                for num1 in range(1, (X.size - 1)):  # for each words in the exact cluster

                    t = Y[num2]
                    count = count + len(re.findall(X[num1], t))
                if (comp<count):
                    comp = count
                    results=X[0]

        if(comp<15):
            category="Nonfintech"
            results="Non-FinTech"
        else:
            category="Fintech"

        with open(path, 'a') as f:
            csv_write = csv.writer(f)
            csv_write.writerow((num2-1,Z[num2],A[num2],results,comp,category))

        print("most words for jobID:",num2-1)
        print("Bank name:", Z[num2])
        print("Job tiltle:", A[num2])
        print("the job belongs to:")
        print (results, "-",comp)
        print (category)
    return;


dsk={'load1' :loading("ClustersList.csv"),
     'load2': loading("LemmatisedData.csv"),
     'run'   :(JobClassification,str1,str2)}
from dask.multiprocessing import get
if __name__ == '__main__':
    str1 = "ClustersList.csv"  # List of different clusters with cluster name as headers
    str2 = "LemmatisedDataS3.csv"  # List of all the jobs from all the 12 teams
    get(dsk, 'run')
