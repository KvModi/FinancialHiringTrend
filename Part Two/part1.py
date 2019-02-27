import os
import pandas as pd
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer


def combineData():
    csv = ['team1.csv', 'team2.csv', 'team3.csv', 'team4.csv', 'team5.csv', 'team6.csv', 'team7.csv', 'team8.csv',
           'team9.csv', 'team10.csv', 'team11a.csv', 'team11b.csv', 'team12.csv']
    df_list = []
    for f in sorted(csv):
        df_list.append(pd.read_csv(f))  # Appending all the csv in df_list List
    full_df = pd.concat(df_list, sort=True)
    full_df.to_csv('24banks.csv')  # Converting the list to CSV file



from nltk.stem import WordNetLemmatizer


def lemmatise():
    aws_id = 'AKIAJ7RQNE26LVIT5UOQ'  # Access key for Amazon S3
    aws_secret = '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'  # Secret key for Amazon S3
    s3 = boto3.client('s3', aws_access_key_id=aws_id, aws_secret_access_key=aws_secret)
    obj = s3.get_object(Bucket='assignment2ds', Key='AllTeamsDraft.csv')
    data = obj['Body'].read()
    samplekeywordclusters = pd.read_csv(io.BytesIO(data), encoding='ISO-8859-1')

    data = pd.read_csv('24banks.csv', encoding='ISO-8859-1')
    data['description'] = data['description'].str.lower()
    clean_data = []
    desc = data['description'].tolist()
    # print(desc[0])
    for i in desc:  # Removing special characters from the job description
        a = re.sub('[^A-Za-z0-9]+', ' ', str(i))
        clean_data.append(a)
    # print('--------------------------------')
    lemmatised_data = []
    j = 0
    for i in clean_data:
        # Tokenizing and lemmatizing the data
        print('Job Number: ' + str(j) + '==================')
        word_list = nltk.word_tokenize(i)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        lemmatised_data.append(lemmatized_output)
        j = j + 1
    # print(lemmatised_data[1])
    data['description'] = lemmatised_data
    data.to_csv('LemmatisedDataS3.csv')

    # To transfer files to amazons3
    client = boto3.client('s3', aws_access_key_id='AKIAJ7RQNE26LVIT5UOQ',
                          aws_secret_access_key='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')
    transfer = S3Transfer(client)
    transfer.upload_file('LemmatisedDataS3.csv', 'assignment2ds', 'LemmatisedDataS3')

if __name__ == '__main__':

#lemmatise()
#combineData()



