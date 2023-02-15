#! python3
# stopwatch.py-Простая программа-хронометр

import time

#Отображение инструкции по использованию программы
print('Чтобы начать отсчет, нажмите клавишу ENTER. Впоследствии для имитации щелчков кнопки секундометра нажимайте клавишу<Enter>.Для выхода из программы нажмите клавиши <Ctrl+C>.')
input() #Нажатие клавиши <Enter> начинает отсчет
print('Отсчет начат')
startTime=time.time() #получение времени начала первого замера
lastTime=startTime
lapNum=1

#Начать отслеживание замеров
try:
    while True:
        input()
        lapTime=round(time.time()-lastTime,2)
        totalTime=round(time.time()-startTime,2)
        print('Замер #%s:%s(%s)'%(lapNum,totalTime,lapTime),end='')
        lapNum+=1
        lastTime=time.time()#переустановить время последнего замера
except KeyboardInterrupt:
    #Обработать исключение <Ctrl+C>, чтобы предотвратить отображение его сообщений
    print('\nГотово.')
