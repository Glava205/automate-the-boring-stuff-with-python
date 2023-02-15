#!python3
#resizeAndAddLogo-Изменяет размеры всех изображений в текущем рабочем каталоге такоим образом,
#чтобы они вписывалтсь в квадрат с размерами 300х300, и добавляет изображение catlogo.png в его нижний правый угол

import os
from PIL import Image

SQUARE_FIT_SIZE=300
lOGO_FILENAME='catlogo.png'

logoIm=Image.open(LOGO_FILENAME)
logoWidth,logoHeight=logoIm.size

os.makedirs('withLogo',exist_ok=True)

#Организовать цикл по всем файлам в текущем рабочем каталоге
for filename in os.listdir('.'):
    if not(filename.endswith('.png')or filename.endswith('.jpg'))or filename==LOGO_FILENAME:
        continue#пропустить файл не являющиеся файлами изображений , и файл самого логотипа
    im=Image.open(filename)
    width,height=im.size

#Проверить, нуждается ли изображение в изменении размеров
    if width>SQUARE_FIT_SIZE and height>SQUARE_FIT_SIZE:
        
#Рассчитать необходимые новые значения ширины и высоты
                if width>height:
            height=int((SQUARE_FIT_SIZE/width)*height)
            width=SQUARE_FIT_SIZE
        else:
            width=int((SQUARE_FIT_SIZE/height)*width)
            height=SQUARE_FIT_SIZE
            
#Изменить размеры изображения
        print('Изменение размеров изображения %s...'%(filename))
        im=im.resize((width,height))

#Добавить логотип
    print('Добавление логотипа в изображение %s...'%(filename))
    im.paste(logoIm,(width-logoWidth,height-logoHeight),logoIm)

#Сохранить изменения
    import.save(os.path.join('withLogo',filename))
