
# This code is to scrape data from a website anput the recorded cases ( infected, reported death, and recovered cases )
# trying to learn scraping and participate on getting updated information for the same
# and may be will be used for later analytics job
# =========================================================================================================================

import requests

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup

import json
import datetime

import os
import errno

folderDateTime = datetime.datetime.today().date().strftime("%d-%m-%Y")


def getWebPage(url):
    """ get the webpage source and save it in a folder with the datetime attribute """

    browser = webdriver.Chrome()
    browser.get(url)

    webPage = browser.page_source

    browser.quit()

    #folderName_1 = datetime.datetime.today().date()

    filename_1 = 'C:/WebScraping-Covid-19/Covid-19 Data - ' + str(folderDateTime) + '/WebPage.html'


    if not os.path.exists(os.path.dirname(filename_1)):
        try:
            os.makedirs(os.path.dirname(filename_1))
        except OSError as exc:
            # Guard against race condition
            if exc.errno != errno.EEXIST:
                    raise

    with open(filename_1, "w", encoding='utf-8') as f:
        f.write(webPage)


    return webPage

def saveData(*DataSet):

    """ To save extracted data in a JSON filesget """

    #folderName_2 = datetime.datetime.today().date()

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


# frequency = datetime.timedelta(1)

# headers_ = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0' }
#
# URL_1 = "https://infographics.channelnewsasia.com/covid-19/map.html?fbclid=IwAR3iXCMrnHQO2KfwbPtK8ogflgSE8Op_l_4ycfGIAJUkdJgaM9lOGK1xioY"
#
#
#
# html_source_1 = getWebPage(URL_1)
#
#
# if html_source_1:
#     soup_1 = BeautifulSoup(html_source_1 ,"html.parser")
#
#
# country_DataSet_1 = soup_1.findAll('div' ,{'class' :'dataDivCol1'})
# print(len(country_DataSet_1))
#
# confirmed_cases_DataSet_1 = soup_1.findAll('div' ,{'class' :'dataDivCol2'})
# print(len(confirmed_cases_DataSet_1))
#
# reported_death_cases_DataSet_1 = soup_1.findAll('div' ,{'class' :'dataDivCol3'})
# print(len(reported_death_cases_DataSet_1))
#
# recovered_cases_DataSet_1 = soup_1.findAll('div' ,{'class' :'dataDivCol4'})
# print(len(recovered_cases_DataSet_1))

# ======================= To store data in json file  ===================


#covid_19_Data_1 = []
#covid_19_Data_1.clear()

#for i in range (1 ,len(country_DataSet_1 ) -1):
#    covid_19_Data_1.append \
#        ({'Country Name': country_DataSet_1[i].text, 'Confirmed Cases': confirmed_cases_DataSet_1[i].text, 'Reported Death': reported_death_cases_DataSet_1[i].text, 'Recovered Cases': recovered_cases_DataSet_1[i].text})

# print json.dumps(covid_19_Data)

#covid_19_Data_json_1 = json.dumps(covid_19_Data_1)

#with open('C:/WebScraping-Covid-19/Covid_19_Data_1.json', 'w', encoding='utf-8') as f:
#    json.dump(covid_19_Data_1, f, ensure_ascii=False, indent=4)

# ===================================================================

# =================  to get data from another website ================


URL_2 = "https://www.worldometers.info/coronavirus/?fbclid=IwAR3Q7nTfpo3flcECajNXURyzoe7H0lPYGGLkjeELWBYJjoVCvjqqjeew6Eg"


html_source_2 = getWebPage(URL_2)


if html_source_2:
    soup_2 = BeautifulSoup(html_source_2 ,"html.parser")

# =========== to get the data, I examined the page and found all data comes under tr tags

covid_19_Data_2 = []
covid_19_Data_2.clear()

# ============ to get all tr Tags

Data_Set_tr_Tags = soup_2.findAll('tr')

for i in range (1 ,len(Data_Set_tr_Tags ) -1):
    # Data_Set_List = ' '.join(Data_Set[i].text.strip().split()).strip().split(' ')
    Data_Set_td_Tags = Data_Set_tr_Tags[i].findAll('td')
	# for j in range(0,len(Data_Set_td_Tags)-1):
    covid_19_Data_2.append({'Country Name': Data_Set_td_Tags[0].text, 'Confirmed Cases': Data_Set_td_Tags[1].text, 'Reported Death': Data_Set_td_Tags[3].text, 'Recovered Cases': Data_Set_td_Tags[5].text})


# ======================= To save data in json file  ===================

saveData(covid_19_Data_2)

# print json.dumps(covid_19_Data)

#covid_19_Data_json_2 = json.dumps(covid_19_Data_2)

#with open('C:/WebScraping-Covid-19/Covid-19/Covid_19_Data_2.json', 'w', encoding='utf-8') as f:
#    json.dump(covid_19_Data_2, f, ensure_ascii=False, indent=4)

# ===================================================================
