import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re
import csv


def call_csvSun(string_csv, list_Number):
    list_suntrust = []
    url_sun = []
    element = []


    f1 = open(string_csv)
    reader = csv.reader(f1)
    #df1 = pd.read_excel(string_csv)

    job_location = []
    job_title = []

    df = pd.read_csv('TextRankFinal.csv')
    analysis = df['customer'].to_list()
    print(analysis)
    #for row in reader:
       # a = analysis.append(row[1])


    for i in range(1, 24):
        job_list_sun_trust = []
        print('==========PAGE' + str(i) + '=====================')
        page = requests.get("https://jobs.suntrust.com/ListJobs/All/Page-" + str(i))
        soup = BeautifulSoup(page.content, "html.parser")
        a_href = soup.find_all('a', href=True)
        job_list = []

        job_desc_a = soup.find_all('td', {'class': 'coldisplayjobid'})
        for i in job_desc_a:
            x = i.find('a', href=True)
            element.append(x.text)

        print(len(element))


        for i in a_href:
            job_list.append(i['href'])
        r = re.compile('ShowJob.*')
        job_list = filter(r.search, job_list)
        job_list = list(set(job_list))


        for jobs in job_list:
            a = "https://jobs.suntrust.com/" + str(jobs)
            job_list_sun_trust.append(a)

        for i in job_list_sun_trust:
            print('==========element ' + str(i) + '=====================')
            # list_words = analysis # Pass list of words from top 100 csv files (lower case)jobdescription-value
            page = requests.get(i)
            url_sun.append(i)
            soup = BeautifulSoup(page.content, "html.parser")
            job_desc = soup.find_all('div', {'class': 'jobdescription-value'})
            #jobID_suntrust = job_desc[3].text
            for title in soup.find_all('div', {'class': 'jobdescription-row jobtitle'}):
                job_title_a = title.find('div', {'class':'jobdescription-value'})
                job_title.append(job_title_a.h1.text)

            for job_loc in soup.find_all('div', {'class': 'jobdescription-row location'}):
                job_loc_a = job_loc.find('div', {'class':'jobdescription-value'})
                job_location.append(job_loc_a.text)


            for i in job_desc[6:]:
                a = i.get_text().lower()

                a = a.translate({ord(c): '' for c in "\.{2,}!@#$%^&*()[]\\{};:,./<>?\|`~-=_+\"\“\”"})

                a = a.split()
                dict_words = {}
                for i in analysis:
                    for j in a:
                        if i == j:
                            if i not in dict_words:
                                dict_words[i] = 0
                            dict_words[i] += 1
            list_suntrust.append(dict_words)
        print(list_suntrust)

    # for key, value in dict_words.items():
    # print(key, value)
    df1 = pd.DataFrame(list_suntrust)

    df1['Job ID'] = element

    df1['Institution'] = 'Suntrust Bank'

    df1['URL'] = url_sun

    df1['list id'] = list_Number
    df1['location'] = job_location
    df1['Job Title'] = job_title

    print(df1)
    cols1 = df1.columns.tolist()
    cols1 = cols1[-6:] + cols1[:-6]
    df1 = df1[cols1]
    print(cols1)
    df1.to_excel('/Users/Nidhi/PycharmProjects/dataScience/SuntrustTextRank.xlsx')


# ============================================== Web Scraping for Discover Financials ===========================================================

list_dictionary = []
job_id = []
job_post = []
url_list = []
location_discover = []
postName = []
a = None


def call_csvDis(string_csv, list_number):

    f2 = open(string_csv)
    a = string_csv
    reader = csv.reader(f2)
    #analysisD = []

    df = pd.read_csv('TF_IDF.csv')
    analysis = df['Column'].to_list()
    print(analysis)

   # for row in reader:
      #  print(row)
        #analysisD.append(row[1])

    dict_words = {}
    driver = webdriver.Chrome(executable_path='/Users/Nidhi/PycharmProjects/chromedriver.exe')

    #list_words = analysisD[0]

    for p in range(1, 28):
        print('page' + str(p) + '----------------------------------------------------------------')
        url = 'https://jobs.discover.com/job-search/?pg=' + str(p)
        driver.get(url)
        for i in range(1, 12):
            text = []
            print('Element' + str(i) + '----------------------------------------------------')
            string_a = ('//*[@id="job-result' + str(i) + '\"' + ']')
            search_google = driver.find_element_by_xpath(string_a)

            driver.execute_script('arguments[0].click();', search_google)
            url_list.append(driver.current_url)
            count = driver.find_element_by_class_name('jddesc')
            a = count.text
            a = a[-11:]
            if re.match(r'^ID:', a):
                a = re.sub('ID:', '', a)
                #print(a)
            job_id.append(a)
            element = driver.find_element_by_class_name("jobdetail-desc")
            text.append(element.text)

            post_in_job = driver.find_element_by_id("gtm-jobdetail-title")
            a = post_in_job.text
            postName.append(a)

            location = driver.find_element_by_class_name("jdlocation")
            location_discover.append(location.text)


            dict_words = {}
            for i in text:
                print('\n' + '\n')
                i = i.lower()
                a = i.translate({ord(c): '' for c in "\.{2,}!@#$%^&*()[]\\{};:,./<>?\|`~-=_+\"\“\”"})
                a = i.split()
                for i in analysis:
                    for j in a:
                        if i == j:
                            if i not in dict_words:
                                dict_words[i] = 0
                            dict_words[i] += 1
            list_dictionary.append(dict_words)
            print('====')
            print(dict_words)
            print('====')
            driver.execute_script("window.history.go(-1)")
            # search_goog = driver.find_element_by_xpath('//*[@id="widget-jobsearch-results-pages"]/a[4]')
            # driver.execute_script('arguments[0].click();', search_goog)
    print(list_number)
    df = pd.DataFrame(list_dictionary)
    df['Job ID'] = job_id
    df['Institution'] = 'Discover Financials'
    df['URL'] = url_list
    df['list id'] = list_number
    df['location'] = location_discover
    df['Job Title'] = postName


    print(df)
    cols = df.columns.tolist()
    cols = cols[-6:] + cols[:-6]
    df = df[cols]
    print(cols)
    df.to_excel('/Users/Nidhi/PycharmProjects/dataScience/DiscoverTFIDFCount.xlsx')


if __name__ == '__main__':
    #call_csvDis('wordcount.csv', 1)
    #call_csvSun('TextRankFinal.csv', 3)
    #call_csvDis('TF_IDF.csv', 2)
    df.duplicated()
