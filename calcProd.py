import time

def calcProd():
    #Вычисление произведения первых чисел 100000 чисел
    product=1
    for i in range(1,100000):
        product=product*i
    return product

startTime=time.time()
prod=calcProd()
endTime=time.time()
print('Длина результата : %s цифр.'%(len(str(prod))))
print('Расчет занял %s секунд.'%(endTime-startTime))
