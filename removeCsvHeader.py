#! python3
# removeCsvHeader.py- Удаляет заголовки из всех CSV-файлов в текущем рабочем катологе

import csv,os

os.makedirs('headerRemoved',exist_ok=True)

#Цикл по всем файлам в текущем рабочем каталоге
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue#пропустить файлы с расширением, отличным от .csv
    print('Удаление заголовка из файла '+csvFilename+'...')
    
    #прочитать CSV-файлы (с пропуском первой строки)
    csvRows=[]
    csvFileObj=open(csvFilename)
    readerObj=csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num==1:
            continue#пропустить первую строку
        csvRows.append(row)
    csvFileObj.close()

    #записать CSV-файл
    csvFileObj=open(os.path.join('headerRemoved',csvFilename),'w',newwline='')
    csvWriter=csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csv.FileObj.close()
