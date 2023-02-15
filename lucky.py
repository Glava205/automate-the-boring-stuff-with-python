#lucky.py-Открывает несколько результатов поиска  помощью Google

import requests,sys,webbrowser,bs4

print('Гуглим...')#отображается при загрузке страницы Google
res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))

res.raise_for_status()

#извлечь первые несколько найденных ссылок
soup=bs4.BeautifulSoup(res.text)

#открыть отдельную вкладку для каждого результата
linkElems=soup.select('.r a')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
