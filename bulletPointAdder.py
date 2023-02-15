#! python3
#bulletPointAdder-Добавляет маркеры Википедии в буфер обмена каждой строки текста, сохраненного в буфере обмена

import pyperclip
text=pyperclip.paste()

#Разделяет строки и добавляет звездочки
lines=text.split('\n')
for i in range(len(lines)):  #цикл по списку "lines"
    lines[i]='* '+lines[i]                #добавляет звездочку в каждую строку в списке "lines"

text='\n'.join(lines)

pyperclip.copy(text)
