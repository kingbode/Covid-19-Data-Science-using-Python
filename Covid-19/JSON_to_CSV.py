import json
import csv
import os

def _Json_to_CSV_(InputFile):

    #ifilename = 'C:\WebScraping-Covid-19\Covid-19 Data - 18-03-2020 23-42\Covid-19 - Extracted Data - 18-03-2020 23-42.json'
    ofilename = InputFile.strip('json')+'csv'
    #C:\WebScraping-Covid-19\Covid-19 Data - 18-03-2020 23-42\Covid-19 - Extracted Data - 18-03-2020 23-42.csv'

    ifile = open(InputFile, 'r', encoding='utf-8')
    ofile = open(ofilename, 'w', encoding='utf-8', newline='') #newline='' removes empty rows
    writer = csv.writer(ofile)

    # this [0] to convert from list to array of rows

    jsonData = json.loads(ifile.read())[0]

    # now you can access each row , or list of data associated for the country as below:

    # jsonData[0] , jsonData[1] Or jsonData[173]


    #with open(ofile, "w", encoding='utf-8') as csv_Out:
    csv_file = csv.writer(ofile)
    csv_file.writerow(["Country Name", "Confirmed Cases", "Reported Death", "Recovered Cases", "Active Cases"])
    for i in range(0, len(jsonData) - 1):
        print(jsonData[i]['Country Name'].strip())
        print(jsonData[i]['Confirmed Cases'].strip())

        csv_file.writerow([jsonData[i]['Country Name'].strip(), jsonData[i]['Confirmed Cases'].strip(),
                           jsonData[i]['Reported Death'].strip(), jsonData[i]['Recovered Cases'].strip(),
                           jsonData[i]['Active Cases'].strip()])

    ofile.close()
    ifile.close()


def get_filepaths(directory):
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

