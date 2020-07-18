import os

# Creating path
os.chdir('D:\\Data_science')

# Getting curret path
os.getcwd()

# Listing files
os.listdir('D:\\Data_science')
os.ls()

# Creating variables
a = 10

# Deleting objects
del a

# Creating directory
os.mkdir('python_folder')

# Creating file

open('python_file.docx','a').close()

# OR
# from pathlib import Path
# path('python2_file.txt').touch()

# copying a file or folder

import shutil, os

shutil.copy('python_file.txt','D:\\Data_science\\python_folder')
shutil.copy('R_folder','D:\\Data_science\\python_folder')

# giving permissions to folder

os.chmod('R_folder',0o444)

# List files in pattern
import glob
glob.glob("*.csv")

# downloading file

import urllib.request

url = "https://www.python.org/static/img/python-logo@2x.png"
urllib.request.urlretrieve(url,'D:\\Data_science\\cat.jpg')

import wget
url = "https://www.python.org/static/img/python-logo@2x.png"
wget.download(url,'D:\\Data_science\\pythonlogo.png')

# Rename directories

os.rename('R_folder','R1_folder')

# Rename files
os.rename('r_file.txt','r1_file.txt')



