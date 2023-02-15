#! python3
# pw.py-программа незащищенного хранения паролей

PASSWORDS={'email':'F7minlBDDuvMJuxESSHFhTxFtjVB6',
           'blog':'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
           'luggage':'12345'}

import sys,pyperclip
if len(sys.argv)<2:
    print('Использование: python pw.py [имя учетной записи] - копирование пароля учетной записи')
    sys.exit()

accountd=sys.argv[1] #первый аргумент командной строки- это имя учетной записи

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для '+account+' скопиован в буфер.')
else:
    print('Учетная запись '+account+' отсутствует в списке.')
