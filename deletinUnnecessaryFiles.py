#Программа для удаления файлов размером больше 100 мб

from send2trash import send2trash 
import os, shutil
 
adr = ''
 
adr = os.path.abspath(adr)
os.chdir(adr)
 
for folder, subfolder, filenames in os.walk(adr):
    for filename in filenames:
        if os.path.getsize(filename)>100000000:
            print(os.path.abspath(filename))
            send2trash(filename)
            
