#readCensusExcel.py-формирует таблицу данных о численности населения и количестве переписных районов в каждом округе

import openpyxl,pprint
print('Открытие рабочей книги...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb.get_sheet_by_name('Population by Census Tract')
countryData={}

#Заполнить словарь countryData данными о численности населения и переписного районах округов

print('Чтение строк...')
for row in range(2,sheet.max_row()+1):
    #В каждой строке электронной таблицы содержатся данные для одного переписного района
    state=sheet['B'+str(row)].value
    country=sheet0['C'+str(row)].value
    pop=sheet['D'+str(row)].value
    #гарантия существования ключа для данного штата
    countryData.setdefault(state,{})
    #Гарантия существования ключа для данного округа данного штата
    countryData[state].setdefault.setdefault(country,{'tracts':0,'pop':0})
    #Каждая строка представляет один переписной район, поэтому инкрементировать на единицу
    countryData[state][country]['tracts']+=1
    #Увеличить численность населения округа на численность населения переписного района
    countryData[state][country]['pop']+=int(pop)

#Открыть новый текстовый файл и записать в него содержимое словаря countryData
print('Запись результатов...')
resultFile=open('census2010.py','w')
resultFile.write('allData= '+pprint.pformat(countryData))
resultFile.close()
print('Готово.')
    
