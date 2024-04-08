import glob
import os
files = glob.glob('./zadanie1/*')
path = './zadanie1/'
for file in files:
    trim_file = file.replace('./zadanie1\\', '')
    try:
        newPath = os.path.join(path, trim_file[0].upper())
        os.mkdir(newPath)
        os.rename(file, f'{newPath}/{trim_file}')
    except:
        newPath = os.path.join(path, trim_file[0].upper())
        os.rename(file, f'{newPath}/{trim_file}')