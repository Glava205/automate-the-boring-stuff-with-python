#! python3
#quickWeather-выводит прогноз погоды для заданного населенного пункта

import json,requests,sys

#Определение названия населенного пункта из аргументов командной строки
if len(sys.argv)<2:
    print('Использование: quickWeather.py location')
    sys.exit()
location=' '.join(sys.argv[1:])

#загрузить Json-данные из API сайта OpenWeather.org
url='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3'%(location)
response=requests.get(url)
response.raise_for_status()

#загрузить Json-данные в переменную Python
weatherData=json.loads(response.text)

#вывод прогноза погоды
w=weatherData['list']
print('Погода сегодня в %s:'%(location))
print(w[0]['weather'][0]['main'],'-',
      w[0]['weather'][0]['description'])
print()
print('Завтра:')
print(w[1]['weather'][0]['main'],'-',
      w[1]['weather'][0]['description'])
print()
print('Послезавтра:')
print(w[2]['weather'][0]['main'],'-',
      w[2]['weather'][0]['description'])
