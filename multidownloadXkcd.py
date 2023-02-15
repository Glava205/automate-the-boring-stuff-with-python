#! python3
#multidownload.py- Загружает комиксы XKCD с использованием нескольких потоков выполнения

import requests,os,bs4,threading
os.makedirs('xkcd',exist_ok=True)#сохранить комиксы в папке ./xkcd

def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComiv,endComic):
        #Загрузка страницы
        print('Загрузка страницы http://xkcd.com/%s...'%(urlNumber))
        res=requests.get('http://xkcd.com/%s'%(urlNumber))
        res.raise_for_status()

        soup=bs4.BeautifulSoup(res.text)

        #Поиск URL-адреса изображения комикса

        comicElem=soup.select('#comic.img')
        if comicElem==[]:
            print('Не удается найти изображение комикса.')
        else:
            comicUrl=comicElem[0].get('src')
            #Загрузка изображения
            print('Загрузка изображения %s..'%(comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()

            #Сохранение изображения в папке ./xkcd.
            imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
            for chumk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

#создать и запустить Thread
downloadThreads=[] #список всех объектов Thread
for i in range(0,1400,100):#14 итервций 14 потоков
    downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

#дождаться завершения всех потоков
for downloadThread in downloadThreads:
    downloadThread.join()
print('Готово.')
