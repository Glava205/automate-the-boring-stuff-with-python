def collatz():
    global number
    if  number%2==0:
        number=int(number/2)
        print(str(number))
    elif number%2==1:
        number=int(3*number+1)
        print(str(number))
    return number

try:
    print('Введите любое число.')
    number=int(input())
    while number!=1:
        collatz()
except ValueError:
    print('Вы ввели не числовую переменную')
