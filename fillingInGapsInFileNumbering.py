import os, shutil, re

our_path = r'C:\Users\admin\Desktop\papka' 
number_of_file = 1 # Задаю стартовую цифру для файла, этакий счетчик
for file in os.listdir(our_path):
    pattern_number = re.compile(r'(\d{1,})\.txt') # Создаю обьект класса 
    mo = re.findall(pattern_number,file) 
    if len(mo) == 0:
        continue # Если файл в нашей папке не содержит подходящего названия мы продолжаем поиск
    else: # В ином случаем сравниваем номер текущего файла с номером который записали ранее как стартовый(счетчик)
        number_of_current_file = mo[0] 
        if int(number_of_current_file) == number_of_file:
            number_of_file += 1 # Если номер сходится то увеличиваем счетчик на 1
        else: # Если не сходится
            if number_of_file < 10: # Переписываю название итерируемого файла согласно цифре счетчика
                new_file_name = os.path.join(our_path, f'spam00{number_of_file}.txt')
                shutil.move((os.path.join(our_path, file)), os.path.join(our_path, new_file_name))
                number_of_file += 1 #Добавляю к счетчику 1
            elif 9 < number_of_file < 100: # Тоже самое в случае если цифра двухзначная
                new_file_name = os.path.join(our_path, f'spam0{number_of_file}.txt')
                shutil.move((os.path.join(our_path, file)), os.path.join(our_path, new_file_name))
                number_of_file += 1 #Добавляю к счетчику 1
            else: # Тоже самое в случае если цифра больше чем двухзначная
                new_file_name = os.path.join(our_path, f'spam{number_of_file}.txt')
                shutil.move((os.path.join(our_path, file)), os.path.join(our_path, new_file_name))
                number_of_file += 1 #Добавляю к счетчику 1
