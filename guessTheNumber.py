import random
print('Мною задумано число от 1 до 20. Попробуйте его угадать.')
num=random.randint(1,20)
counter=0
while True:
    print('Ваш вариант:')
    res=int(input())
    if res<num:
        print('Предложенное число меньше задуманного')
    elif res>num:
        print('Предложенное число больше задуманного')
    elif res==num:
        print('Верно!')
        counter=counter+1
        break
    counter=counter+1
print('Количество попыток:'+str(counter))
    
