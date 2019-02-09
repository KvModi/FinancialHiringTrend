# FinancialHiringTrend


This project was created to analyse the hiring trend at the current time (February 06, 2019) in the two banks: SunTrust Bank and Discover Financials.
For this objective, following steps are performed:
1. merger.py
  Merging the 4 pdf files which are the research conducted by The World Economic forum in the field of FinTech: 
   a. http://www3.weforum.org/docs/Beyond_Fintech_-_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services.pdf
   b. http://www3.weforum.org/docs/WEF_The_future__of_financial_services.pdf
   c. http://www3.weforum.org/docs/WEF_The_future_of_financial_infrastructure.pdf
   d. http://www3.weforum.org/docs/WEF_A_Blueprint_for_Digital_Identity.pdf
  The output of the file is result.pdf
 
2. toclean.py
    The data obtained in the first step has to be cleaned, i.e. the stopwords like the, and, etc has to be removed along with     the puntuations. The words are lemmatized and filtered.
    The output file is processed_text.txt
  
3. tocsv.py
   The processed_text has to be converted in the csv file so that the words can be sorted as per the requirement.
   The output file is wordlist.csv
  
4. countWords.py
   This file reads the wordlist.csv and sorts the words in the order it is repated the most. The frequency of each word is        stored with it. We pick the top 100 words and save it in the topcount.csv
   
5. tfidf.py
    This file reads the wordlist.csv and pick the top 100 words based TF/IDF which calculates the weightage of words and sves     it in ifcount.csv
    
6. totextrank.py
   This file reads the wordlist.csv and the top 100 words based on textrank is stored in textRankList.csv 
   
7. webScraping.py
   This file beautifulsoup and selenium to webscrape the career sites to gather details of jobs of SunTrust Bank and Discover    Finncial based on theords from the word count, textrank and TF/IDF list s
   The output files are:   DiscoverTextRank.xlsx, DiscoverTFIDFCount.xlsx, DiscoverWordCountFinal.xlsx
                           SuntrustTextRank.xlsx, SuntrustTFIDFCount.xlsx, SuntrustWordCountFinal.xlsx
                           
8. DataFramesConcat.py
   This file concatinate the previous 6 files into one DataFrame for the analysis. The output file is FinTechDataFrame.xlsx
  
9. Data Studio
   The graphical analysis was made using the Data Studio. On the time of this project, SunTrust Bank is hiring more employees than Discover Financials. The hiring of SunTrust Bank is more focused in Southern East area of USA where as hiring in Central America. Both the banks are interested in hiring employes skilled in the field of finance, management, FIS and Tech Security.
