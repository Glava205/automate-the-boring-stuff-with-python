#mapIt-Запускает карту в браузере извлекая почтовый адрес из клмандной строки или буфера обмена

import webbrowser,sys,pyperclip
if len(sys.argv)>1:
    #Получение почтового адреса из командной строки
    address=' '.join(sys.argv[1:])
else:
    #Получить почтовый адрес из буфера обмена
    address=pyperclip.paste()

webbrowser.open('https://www.google/maps/place/'+address)
