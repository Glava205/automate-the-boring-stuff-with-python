#!python3
#mouseNow.py-Отображает текущую позицию указателя мыши

import pyautogui
print('Для выхода нажмите клавиши <Ctrl+C>.')
#получить и вывести координаты указателя мыши
try:
    while True:
        #Получить и вывести координаты указателя мыши
        x,y=pyautogui.position()
        positionStr='X: '+str(x).rjust(4)+ ' Y: '+str(y).rjust(4)
        pixelColor=pyautogui.screenshot().getpixel((x,y))
        positionStr+=' RGB: ('+str(pixelColor[0]).rjust(3)
        positionStr+=', '+str(pixelColor[1]).rjust(3)
        positionStr+=', '+str(pixelColor[2]).rjust(3)+')'
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)

except KeyboardInterrupt:
    print('\nГотово.')
