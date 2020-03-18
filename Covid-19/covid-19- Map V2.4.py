
# This code is to scrape data from a website anput the recorded cases ( infected, reported death, and recovered cases )
# trying to learn scraping and participate on getting updated information for the same
# and may be will be used for later analytics job
# =========================================================================================================================

import requests

from selenium import webdriver  
from bs4 import BeautifulSoup

import json
import datetime

import os
import errno

folderDateTime = datetime.datetime.today().date().strftime("%d-%m-%Y ") + datetime.datetime.today().time().strftime("%H-%M")


def getWebPage(url):
    """ get the webpage source and save it in a folder with the datetime attribute """

    browser = webdriver.Chrome()
    browser.get(url)

    webPage = browser.page_source

    browser.quit()

    filename_1 = 'C:/WebScraping-Covid-19/Covid-19 Data - ' + str(folderDateTime) + '/WebPage.html'


    if not os.path.exists(os.path.dirname(filename_1)):
        try:
            os.makedirs(os.path.dirname(filename_1))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                    raise

    with open(filename_1, "w", encoding='utf-8') as f:
        f.write(webPage)


    return webPage

def saveData(*DataSet):

    """ To save extracted data in a JSON file """

    filename_2 = 'C:/WebScraping-Covid-19/Covid-19 Data - ' + str(folderDateTime) + '/Covid-19 - Extracted Data - ' + str(folderDateTime) + '.json'


    if not os.path.exists(os.path.dirname(filename_2)):
        try:
            os.makedirs(os.path.dirname(filename_2))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename_2, "w", encoding='utf-8') as f:
        json.dump(DataSet, f, ensure_ascii=False, indent=4)

    return 0

# ===================================================================

# =================  to get data from another website ================


URL_2 = "https://www.worldometers.info/coronavirus/?fbclid=IwAR3Q7nTfpo3flcECajNXURyzoe7H0lPYGGLkjeELWBYJjoVCvjqqjeew6Eg"


html_source_2 = getWebPage(URL_2)


if html_source_2:
    soup_2 = BeautifulSoup(html_source_2 ,"html.parser")

# =========== to get the data, I examined the page and found all data comes under tr tags

covid_19_Data = []
covid_19_Data.clear()

# ============ to get all tr Tags

Data_Set_tr_Tags = soup_2.findAll('tr')
#print(len(Data_Set_tr_Tags))

for i in range (1 , 175 ): #len(Data_Set_tr_Tags ) -1):
    #if i==172:
    #   print(i)
    Data_Set_td_Tags = Data_Set_tr_Tags[i].findAll('td')
    #print(i, Data_Set_td_Tags[0].text,Data_Set_td_Tags[1].text,Data_Set_td_Tags[3].text,Data_Set_td_Tags[5].text)
    if len(Data_Set_td_Tags) == 9: #len(Data_Set_tr_Tags[i-1].findAll('td')):
        # check_Element = {'Country Name': Data_Set_td_Tags[0].text, 'Confirmed Cases': Data_Set_td_Tags[1].text,'Reported Death': Data_Set_td_Tags[3].text, 'Recovered Cases': Data_Set_td_Tags[5].text}
        # if  check_Element not in covid_19_Data_2 :
            covid_19_Data.append({'Country Name': Data_Set_td_Tags[0].text, 'Confirmed Cases': Data_Set_td_Tags[1].text,'Reported Death': Data_Set_td_Tags[3].text, 'Recovered Cases': Data_Set_td_Tags[5].text})


# ======================= To save data in json file  ===================

saveData(covid_19_Data)

# ===================================================================
