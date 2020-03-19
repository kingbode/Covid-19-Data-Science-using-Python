
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

folderDateTime = datetime.datetime.today().date().strftime("%d-%m-%Y ") + datetime.datetime.today().time().strftime("%H-%M")

fullPath = 'C:/WebScraping-Covid-19/Covid-19 Data - ' + str(folderDateTime)





def getWebPage(url):
    """ get the webpage source and save it in a folder with the datetime attribute """
    # options to start Chrome in headless mode.
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    browser = webdriver.Chrome(chrome_options=options)

    #chrome_options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
    #browser = webdriver.Chrome()#executable_path=os.path.abspath(“chromedriver"), chrome_options = chrome_options)
    #browser = webdriver.PhantomJS() # webdriver.Chrome()
    browser.get(url)

    webPage = browser.page_source

    browser.quit()

    webPage_filename = fullPath + '/WebPage.html'


    if not os.path.exists(os.path.dirname(webPage_filename)):
        try:
            os.makedirs(os.path.dirname(webPage_filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                    raise

    with open(webPage_filename, "w", encoding='utf-8') as f:
        f.write(webPage)


    return webPage

def saveData(*DataSet):

    """ To save extracted data in a JSON file """

    JSON_Data_filename = fullPath + '/Covid-19 - Extracted Data - ' + str(folderDateTime) + '.json'


    if not os.path.exists(os.path.dirname(JSON_Data_filename)):
        try:
            os.makedirs(os.path.dirname(JSON_Data_filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(JSON_Data_filename, "w", encoding='utf-8') as f:
        json.dump(DataSet, f, ensure_ascii=False, indent=4)

    return 0

# ===================================================================

# =================  to get data from another website ================

#================== Main ===============================
#=======================================================

URL = "https://www.worldometers.info/coronavirus/?fbclid=IwAR3Q7nTfpo3flcECajNXURyzoe7H0lPYGGLkjeELWBYJjoVCvjqqjeew6Eg"


print('Getting latest Corona Virus Updates from World Meter Website')
print('============================================================')
print(URL)
print('============================================================')

html_source = getWebPage(URL)


print('============================================================')
print('Saving Data ....')


if html_source:
    soup = BeautifulSoup(html_source ,"html.parser")
    print('Data has been downloaded successfully')


# =========== to get the data, I examined the page and found all data comes under tr tags

covid_19_Data = []
covid_19_Data.clear()

# ============ to get all tr Tags

Data_Set_tr_Tags = soup.findAll('tr')
#print(len(Data_Set_tr_Tags))

Check_if_reached_Total = ''

for i in range (1 , len(Data_Set_tr_Tags ) -1):
    #if i==174:
    #   print(i)
    if Check_if_reached_Total == 'Total:':
        pass
        # this check to avoid reading more data that are hidden on the webpage and stores previuos reads !!! , may be used by the website
        break
    Data_Set_td_Tags = Data_Set_tr_Tags[i].findAll('td')
    #print(i, Data_Set_td_Tags[0].text,Data_Set_td_Tags[1].text,Data_Set_td_Tags[3].text,Data_Set_td_Tags[5].text)
    if len(Data_Set_td_Tags) == 9: #len(Data_Set_tr_Tags[i-1].findAll('td')):
        # check_Element = {'Country Name': Data_Set_td_Tags[0].text, 'Confirmed Cases': Data_Set_td_Tags[1].text,'Reported Death': Data_Set_td_Tags[3].text, 'Recovered Cases': Data_Set_td_Tags[5].text}
        # if  check_Element not in covid_19_Data_2 :
        covid_19_Data.append({'Country Name': Data_Set_td_Tags[0].text.strip(), 'Confirmed Cases': Data_Set_td_Tags[1].text.strip(),'Reported Death': Data_Set_td_Tags[3].text.strip(), 'Recovered Cases': Data_Set_td_Tags[5].text.strip() , 'Active Cases': Data_Set_td_Tags[6].text.strip()})
        Check_if_reached_Total = Data_Set_td_Tags[0].text.strip()




# ======================= To save data in json file  ===================

saveData(covid_19_Data)

print('Data has been saved ....')

# ===================================================================
