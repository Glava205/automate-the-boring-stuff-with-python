#renameDates-еременовывает файлы имена которых включают даты указанные в американском формате(ММ-ДД-ГГГГ)приводя их в соответствие с европейским форматом дат(ДД-ММ-ГГГГ)

import shutil,os,re

#создание регулярного выражения которому соответствуют именя файов содержащие даты в американском формате
datePattern=re.compile(r"""^(.*?) #весь текст перед датой
((0|1)?\d)-                                 #одна или две цифры месяца
((0|1|2|3)?\d)-                             #одна или две цифры числа
((19|20)\d\d)                               #четыре цифры года
(.*?)$                                           #весь текст после даты
 """,re.VERBOSE)

#организовать цикл по файлам в рабочем катологе
for amerFilename in os.listdir('.'):
    mo=datePattern.search(amerFilename)

    #пропустить файлы с именами не содержащими дат
    if mo==None:
        continue

    #получить отдельные части имен файлов
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)

    #сформировать имена соответствующие европейскому стилю укащания дат
    euroFilename=beforePart+'-'+monthPart+'-'+yearPart=afterPart

    #получить полные абсолютные пути к файлам
    absWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)

    #переименовать файлы
    print('Заменяем имя "%s" именем "%s"...'%(amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename)
    #раскоментировать после выполнения тестирования
