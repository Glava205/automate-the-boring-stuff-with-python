#! python3
# countdown.py-Простой сценарий обратного отсчета

import time, subprocess

timeLeft=60
while timeLeft>0:
    print(timeLeft,end=' ')
    time.sleep(1)
    timeLeft=timeLeft-1

#Воспроизвести звуковой файл по завершении обратного отсчета
subprocess.Popen(['start','alarm.wav'],shell=True)
