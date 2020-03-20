
""" This Class has some functions that are used in Main application """


""" Function        : Description """
""" _Json_to_CSV_   : Takes input argment ( JSON file and convert it o CSV file in same folder with same name but with csv extension """

""" 
_get_filepaths   :  This function will generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each
directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
"""

""" _save_Data_to_JSON: function that takes data list (array) and save it in JSON file """

import csv
import errno
import json
import os

from selenium import webdriver


def _Json_to_CSV_(InputFile):

    """ _Json_to_CSV_   : Takes input argment ( JSON file and convert it o CSV file in same folder with same name but with csv extension """

    ofilename = InputFile.strip('json')+'csv'

    ifile = open(InputFile, 'r', encoding='utf-8')
    ofile = open(ofilename, 'w', encoding='utf-8', newline='') #newline='' removes empty rows
    writer = csv.writer(ofile)

    # this [0] to convert from list to array of rows !!!

    jsonData = json.loads(ifile.read())[0]

    # now you can access each row , or list of data associated for the country as below:

    # jsonData[0] , jsonData[1] Or jsonData[173]


    #with open(ofile, "w", encoding='utf-8') as csv_Out:
    csv_file = csv.writer(ofile)
    csv_file.writerow(["Country Name", "Confirmed Cases", "Reported Death", "Recovered Cases", "Active Cases"])
    for i in range(0, len(jsonData) - 1):
        #print(jsonData[i]['Country Name'].strip())
        #print(jsonData[i]['Confirmed Cases'].strip())

        csv_file.writerow([jsonData[i]['Country Name'].strip(), jsonData[i]['Confirmed Cases'].strip(),
                           jsonData[i]['Reported Death'].strip(), jsonData[i]['Recovered Cases'].strip(),
                           jsonData[i]['Active Cases'].strip()])

    ofile.close()
    ifile.close()

def _save_Data_to_JSON(JSON_filename_, *DataSet):

    """ save_Data_to_JSON: function that takes data list (array) and save it in JSON file """

    if not os.path.exists(os.path.dirname(JSON_filename_)):
        try:
            os.makedirs(os.path.dirname(JSON_filename_))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(JSON_filename_, "w", encoding='utf-8') as f:
        json.dump(DataSet, f, ensure_ascii=False, indent=4)

    f.close()



def _get_WebPage_Source_(url,webPage_filename):
    """ get the webpage source and save it in a folder with the datetime attribute """
    # options to start Chrome in headless mode.
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')

    browser = webdriver.Chrome(chrome_options=options)

    #browser = webdriver.Chrome() #executable_path=os.path.abspath(“chromedriver"), chrome_options = chrome_options)
    #browser = webdriver.Chrome()
    browser.get(url)

    webPage = browser.page_source

    browser.quit()


    if not os.path.exists(os.path.dirname(webPage_filename)):
        try:
            os.makedirs(os.path.dirname(webPage_filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                    raise

    with open(webPage_filename, "w", encoding='utf-8') as f:
        f.write(webPage)

    return webPage

def _get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
# full_file_paths = get_filepaths("C:\WebScraping-Covid-19")
#
# for f in full_file_paths:
#     if f.endswith(".json"):
#         _Json_to_CSV_(f)

