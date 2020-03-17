

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
import re


headers_ = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0' }

URL_1 = "https://infographics.channelnewsasia.com/covid-19/map.html?fbclid=IwAR3iXCMrnHQO2KfwbPtK8ogflgSE8Op_l_4ycfGIAJUkdJgaM9lOGK1xioY"


browser = webdriver.Chrome()

browser.get(URL_1)


html_source_1 = browser.page_source  
browser.quit()

if html_source_1:
	soup_1 = BeautifulSoup(html_source_1,"html.parser")


country_DataSet_1 = soup_1.findAll('div',{'class':'dataDivCol1'})
print(len(country_DataSet_1))

confirmed_cases_DataSet_1 = soup_1.findAll('div',{'class':'dataDivCol2'})
print(len(confirmed_cases_DataSet_1))

reported_death_cases_DataSet_1 = soup_1.findAll('div',{'class':'dataDivCol3'})
print(len(reported_death_cases_DataSet_1))

recovered_cases_DataSet_1 = soup_1.findAll('div',{'class':'dataDivCol4'})
print(len(recovered_cases_DataSet_1))



#======================= To store data in json file  ===================


covid_19_Data_1 = []
covid_19_Data_1.clear()

for i in range (1,len(country_DataSet)-1):
	covid_19_Data_1.append({'Country Name': country_DataSet_1[i].text, 'Confirmed Cases': confirmed_cases_DataSet_1[i].text, 'Reported Death': reported_death_cases_DataSet_1[i].text, 'Recovered Cases': recovered_cases_DataSet_1[i].text})

#print json.dumps(covid_19_Data)

covid_19_Data_json_1 = json.dumps(covid_19_Data_1)

with open('C:/Covid_19_Data_1.json', 'w', encoding='utf-8') as f:
    json.dump(covid_19_Data_1, f, ensure_ascii=False, indent=4)



#===================================================================

#=================  to get data from another website ================

headers_ = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0' }

URL_2 = "https://www.worldometers.info/coronavirus/?fbclid=IwAR3Q7nTfpo3flcECajNXURyzoe7H0lPYGGLkjeELWBYJjoVCvjqqjeew6Eg"


browser = webdriver.Chrome()

browser.get(URL_2)


html_source_2 = browser.page_source  
browser.quit()


if html_source_2:
	soup_2 = BeautifulSoup(html_source_2,"html.parser")


#=========== to get the data, I examined the page and found all data comes under tr tags

# Data_Set = soup_2.findAll('tr')

#========= example
# len(Data_Set)
# 165
# Data_Set[0]
#<tr> <th width="100">Country,<br/>Other</th> <th width="20">Total<br/>Cases</th> <!--<th width="20">%&nbsp;of&nbsp;All<br />Cases</th>--> <th width="30">New<br/>Cases</th> <th width="30">Total<br/>Deaths</th> <th width="30">New<br/>Deaths</th> <th width="30">Total<br/>Recovered</th> <!--<th width="30">New<br />Recovered</th>--> <th width="30">Active<br/>Cases</th> <th width="30">Serious,<br/>Critical</th> <!--<th width="30">Death<br />Rate</th> --> <th width="30">Tot Cases/<br/>1M pop</th> </tr>

#Data_Set[0].text
#' Country,Other TotalCases  NewCases TotalDeaths NewDeaths TotalRecovered  ActiveCases Serious,Critical  Tot\xa0Cases/1M pop '

# Data_Set[1].text
#'  China  80,880   +36   3,213  +14  67,819    9,848  3,226   56.2 '
#==================

#======== now strip spaces and split data and save them in a list to use later ==========

# Data_Set_List = ' '.join(Data_Set[1].text.strip().split()).strip()

# output: 'China 80,880 +36 3,213 +14 67,819 9,848 3,226 56.2'

# Data_Set_List = Data_Set_List.split(' ')

# output: ['China', '80,880', '+36', '3,213', '+14', '67,819', '9,848', '3,226', '56.2']

#================ there is a better way to get td Tags under tr Tags by fidning all td Tags in each tr Tag , so easy and precise !!!


#country_DataSet_2 = Data_Set_List[0]

#confirmed_cases_DataSet_2 = Data_Set_List[1]

#reported_death_cases_DataSet_1 = Data_Set_List[3]

#recovered_cases_DataSet_2 = Data_Set_List[5]


#======================= To store data in json file  ===================


covid_19_Data_2 = []
covid_19_Data_2.clear()

#============ to get all tr Tags

Data_Set_tr_Tags = soup_2.findAll('tr')

for i in range (1,len(Data_Set_tr_Tags)-1):
	# Data_Set_List = ' '.join(Data_Set[i].text.strip().split()).strip().split(' ')
	Data_Set_td_Tags = Data_Set_tr_Tags[i].findAll('td')
	for j in range(0,len(Data_Set_td_Tags)-1):
		covid_19_Data_2.append({'Country Name': Data_Set_td_Tags[0].text, 'Confirmed Cases': Data_Set_td_Tags[1].text, 'Reported Death': Data_Set_td_Tags[3].text, 'Recovered Cases': Data_Set_td_Tags[5].text})

#print json.dumps(covid_19_Data)

covid_19_Data_json_2 = json.dumps(covid_19_Data_2)

with open('C:/Users/Daizer/Desktop/Python codes/WebScraping-Covid-19/Covid-19/Covid_19_Data_2.json', 'w', encoding='utf-8') as f:
    json.dump(covid_19_Data_2, f, ensure_ascii=False, indent=4)



#===================================================================
