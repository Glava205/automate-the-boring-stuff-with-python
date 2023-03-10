#downloadXkcd.py Загружает все комиксы XKCD

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...'% url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Comic img could not be found')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Dowloading image %s...'% (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
