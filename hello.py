#Эта программа приветствует пользователя и запрашивает
#ввод информации

print('Hello world')
print('What os your name?')#запрос имени
myName=input()
print('It is good to meet you, '+myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge=input()
print('You will be '+str(int(myAge)+1)+' in a year.')
