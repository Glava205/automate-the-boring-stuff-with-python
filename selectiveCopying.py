#Программа для выборочного копирования файлов с заданным расширением
 
import os, shutil
 
adr = input('Задайте путь для поиска *.pdf файлов  и *.jpg файлов и копирования по новому адресу - ')
 
adr = os.path.abspath(adr)
os.chdir(adr)
 
for folder, subfolder, filenames in os.walk(adr):
    for filename in filenames:
        if filename.endswith('.pdf')or filename.endswith('.jpg'):
            shutil.copy(filename, '')
