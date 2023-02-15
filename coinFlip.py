import random
guess=''
while guess not in (1,0):
    print('Угадайте результат подбрасывания монеты!.Введите орел(1) или решка(0):')
    guess=int(input())
    if guess==1:
        guess=1
    elif guess==0:
        guess=0
    else:
        continue

toss=random.randint(0,1)#0-решка 1-орел
if toss==guess:
    print('Есть!')
else:
    print('Увы! Неправильный ответ.')
