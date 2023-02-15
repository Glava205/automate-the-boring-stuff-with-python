import re


pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')

print('Введите пароль:')
pwd=str(input())

print(bool(pattern_password.match(pwd)))
