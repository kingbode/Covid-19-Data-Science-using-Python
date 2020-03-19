# Web-Scraping , for covid-19 statistics:

To get Data from Internet about Covid-19 Virus

v2.1:

from below website regarding Covid-19 Virus spreading statistics
Like:
Country , Recorded cases , Reported Death cases , Recovered cases

the link of the wab page is 

https://infographics.channelnewsasia.com/covid-19/map.html?fbclid=IwAR3iXCMrnHQO2KfwbPtK8ogflgSE8Op_l_4ycfGIAJUkdJgaM9lOGK1xioY

and this is to learn how to scrape data from Internet and to get quicker information insight and may be will be used later for 
data analytics.

1- now successfully achieved pulling infomration about Country , Recorded cases , Reported Death cases , Recovered cases and Active cases.
2- these data was under div Tags in the html source.
3- saving these data to JSON file.

=====================================
v2.2:

Trying to get data from another website which seems to have more accurate and live data

https://www.worldometers.info/coronavirus/?fbclid=IwAR3Q7nTfpo3flcECajNXURyzoe7H0lPYGGLkjeELWBYJjoVCvjqqjeew6Eg"

1- now successfully achieved pulling infomration about Country , Recorded cases , Reported Death cases , Recovered cases.
2- these data was under tr and td Tags in the html source.
3- saving these data to JSON file.
4- Now we need to Run the code on periodic basis and store the results to track the variance , done in ver 2.4.

=====================================
V2.4:

- Added date and time to save the webpage that has the data along with extracted data in a separate folder with date and time attributes, so later we could work on all files and detect the variance in data.
- using Headless broswer ( hidden mode )
- Adding messgaes that show the progress of the code.
- saving data in csv file format as well.
- updating all previous data in json file format to be in csv file format as well, this is to prepare for merging data and analysis in later updates.

=====================================
Working on below:

1- Do some analysis and predictions <======== still working on it.
