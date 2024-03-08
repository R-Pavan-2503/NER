import zipfile
import os, fnmatch
import re
from zipfile import ZipFile

path = os.getcwd()

listOfFiles = os.listdir('.')
pattern = "*_j.zip"

for files in listOfFiles:
        if fnmatch.fnmatch(files, pattern):
                filename = re.sub(".zip", ".xml", files)
                filepath = path + "\\" + files
                print (filepath)
                with ZipFile(filepath) as zip:
                    zip.extract(filename, 'F:\PYTHON\INTERN\extracted_xml')