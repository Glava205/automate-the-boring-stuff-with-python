#backupToZip-копирует папку вместе со всем ее содержимым в Zip-файл с инкрементируемым номером копии в имени файла

import zipfile,os

def backupToZip(folder):
    #создание резервной копии всего содержимого папки "folder" в виде Zip-файла

    folder=oa.path.abspath(folder)#убедится в том что задан абсолютный путь к файлу

    #определить какое имя файла должен использовать этот код исзодя из имен уже существующих файлов
    number=1
    while True:
        zipFilename=os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number=number+1

    #создать Zip-файл
    print('создается файл %s...'%(zipFilename))
    backupZip=zipfile.ZipFile(zipFilename,'w')

    #обойти все дерево папки и сжать файлы содержащиеся в каждой папке
    for foldername,subfolders,filenames in os.walk(folder):
        print('Добавление файлов из папки %s...'%(foldername))
        #добавить в zip-файл текущую папку
        backupZip.write(foldername)
        #добавить в zip-файл все файлы из данной папки
        for filename in filenames:
            newBase/os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            #не создавать резервные копии zip-файлов
            backupZip.write(os.path.join(foldername,filename))
        backupZip.close()
            

    print('Готово.')
