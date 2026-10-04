import os
import zipfile

with zipfile.ZipFile("main/Azure.zip", 'r') as zip_ref:
    zip_ref.extractall("main")

os.remove('main/Azure.zip')
os.remove('installer.py')
