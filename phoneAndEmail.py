#phoneAndEmail-Находит телефонные номера и
#адреса электронной почты в буфере обмнена

import pyperclip,re

phoneRegex=re.compile(r'''(
(\d{3}|\(\d{3}\))? #территориальный код
(\s|-|\.)?                        #разделитель
\d{3}                             #первые 3 цифры
(\s|-|\.)                         #разделитель
\d{4}                          #последние 4 цифры
(\s*(ext|x|ext.)\s*(\d{2,5}))? #добавочный номер
)''',re.VERBOSE)

# Создать регулярное выражение для адресов эл почты
emailRegex=re.compile(r'''(
[a-zA-Z0-9._%+-]+ #имя пользователя
@ #символ@
[a-zA-Z0-9.-]+ #имя домена
(\.[a-zA-Z]{2,4}) #остальная часть адреса
)''',re.VERBOSE)


# найти соответствия содержащиеся в буфере обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
   # if groups[8] in groups:
    #    phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# скопировать результаты в буфер обмена
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса книг не обнаружены')
