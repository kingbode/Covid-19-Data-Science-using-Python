
# This code is to scrape data from a website about the recorded cases ( infected, reported death, and recovered cases )
# trying to learn scraping and participate on getting updated information for the same
# and may be will be used for later analytics job
# =========================================================================================================================

import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import json
import datetime

import os
import errno
from __Functions__ import _Json_to_CSV_, _save_Data_to_JSON, _get_WebPage_Source_, _concatenate_CSV_, _get_filepaths

date_ = datetime.datetime.today().date().strftime("%d-%m-%Y")
time_ = datetime.datetime.today().time().strftime("%H-%M")

folderDateTime = date_ + ' ' + time_


fullPath = 'C:/WebScraping-Covid-19/Data/Covid-19 Data - ' + str(folderDateTime) + '/'

webPage_filename = fullPath + 'www.worldometers.info-coronavirus - '+ folderDateTime +'.html'

JSON_Data_filename = fullPath + 'Covid-19 - Extracted Data - ' + str(folderDateTime) + '.json'

Aggregated_CSV_filename = 'c:\WebScraping-Covid-19\Aggregated_Data.csv'



#=======================================================
#================== Main ===============================
#=======================================================

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR3Q7nTfpo3flcECajNXURyzoe7H0lPYGGLkjeELWBYJjoVCvjqqjeew6Eg"


print('Getting latest Corona Virus Updates from World Meter Website')
print('============================================================')
print(URL)
print('============================================================')


print('WebPage for above site is saved for offline analysis in case required... please wait')
print('============================================================')

html_source = _get_WebPage_Source_(URL,webPage_filename)

print('Job is Done... WebPage for above site is saved in this folder\\file '+ webPage_filename)
print('============================================================')

print('Now Data is being extracted .... please wait')




if html_source:
    soup = BeautifulSoup(html_source ,"html.parser")
    print('Data has been downloaded successfully')


# =========== to get the data, I examined the page and found all data comes under tr tags

covid_19_Data = []
covid_19_Data.clear()

# Web Scraping job ....
# ============ to get all tr Tags

Data_Set_tr_Tags = soup.findAll('tr')
#print(len(Data_Set_tr_Tags))

Check_if_reached_Total = ''

for i in range (1 , len(Data_Set_tr_Tags ) -1):
    # used for debug
    #if i==183:
    #   print(i)
    if Check_if_reached_Total == 'Total:':
        pass
        # this check is to avoid reading more data that are hidden on the webpage and stores previuos reads !!! , may be used by the website
        break
    Data_Set_td_Tags = Data_Set_tr_Tags[i].findAll('td')
    #print(i, Data_Set_td_Tags[0].text,Data_Set_td_Tags[1].text,Data_Set_td_Tags[3].text,Data_Set_td_Tags[5].text)
    if len(Data_Set_td_Tags) == 9: #len(Data_Set_tr_Tags[i-1].findAll('td')):
        covid_19_Data.append({'Country Name': Data_Set_td_Tags[0].text.strip(),
                              'Confirmed Cases': Data_Set_td_Tags[1].text.strip(),
                              'Reported Death': Data_Set_td_Tags[3].text.strip(),
                              'Recovered Cases': Data_Set_td_Tags[5].text.strip(),
                              'Active Cases': Data_Set_td_Tags[6].text.strip(),
                              'Date' : date_,
                              'Time' : datetime.datetime.strptime(time_ , "%H-%M").time().strftime("%H:%M")})

        Check_if_reached_Total = Data_Set_td_Tags[0].text.strip()


#=======================================================================

# ======================= To save data in json file  ===================

_save_Data_to_JSON(JSON_Data_filename , covid_19_Data )

_Json_to_CSV_(JSON_Data_filename)

print('Job is Done... Data has been extracted and saved in json and csv file formats in below folder\\files ....')

print(JSON_Data_filename)
print(JSON_Data_filename.strip('.json') + '.csv')
print('============================================================')


print('Now to aggregate all data into one file in ' , Aggregated_CSV_filename)
print('============================================================')


""" this is to aggregate CSV files into one file 'c:\WebScraping-Covid-19\Aggregated_Data.csv' """

CSV_file_list = []
CSV_files = _get_filepaths('c:\WebScraping-Covid-19\Data\\')

for i in range(0,len(CSV_files)-1):
    if CSV_files[i].endswith('.csv'):
        CSV_file_list.append(CSV_files[i])

# print(CSV_file_list)
_concatenate_CSV_(CSV_file_list,Aggregated_CSV_filename)

print('Data Aggregation is done .... ')
# ===================================================================
