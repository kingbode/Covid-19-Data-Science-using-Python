

# This code is to scrape data from a website anput the recorded cases ( infected, reported death, and recovered cases )
# trying to learn scraping and participate on getting updated information for the same
# and may be will be used for later analytics job
#=========================================================================================================================


import requests

from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup

import json



headers_ = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0' }

URL = "https://infographics.channelnewsasia.com/covid-19/map.html?fbclid=IwAR3iXCMrnHQO2KfwbPtK8ogflgSE8Op_l_4ycfGIAJUkdJgaM9lOGK1xioY"


browser = webdriver.Chrome()

browser.get(URL)


html_source = browser.page_source  
browser.quit()

soup = BeautifulSoup(html_source,"html.parser")

country_DataSet = soup.findAll('div',{'class':'dataDivCol1'})
print(len(country_DataSet))

confirmed_cases_DataSet = soup.findAll('div',{'class':'dataDivCol2'})
print(len(confirmed_cases_DataSet))

reported_death_cases_DataSet = soup.findAll('div',{'class':'dataDivCol3'})
print(len(reported_death_cases_DataSet))

recovered_cases_DataSet = soup.findAll('div',{'class':'dataDivCol4'})
print(len(recovered_cases_DataSet))



#{"gsx$admin":{"$t":"Aruba"},"gsx$longitude":{"$t":"-69.98267711"}
Country_DataSet_Location = soup.findAll('var countries')
print(len(recovered_cases_DataSet))



covid_19_Data.clear()
covid_19_Data = []


for i in range (1,len(country_DataSet)-1):
	covid_19_Data.append({'Country Name': country_DataSet[i].text, 'Confirmed Cases': confirmed_cases_DataSet[i].text, 'Reported Death': reported_death_cases_DataSet[i].text, 'Recovered Cases': recovered_cases_DataSet[i].text})

#print json.dumps(covid_19_Data)

covid_19_Data_json = json.dumps(covid_19_Data)

with open('C:/Covid_19_Data.json', 'w', encoding='utf-8') as f:
    json.dump(covid_19_Data, f, ensure_ascii=False, indent=4)

