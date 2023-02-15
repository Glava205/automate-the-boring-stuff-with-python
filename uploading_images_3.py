import requests

p = requests.get(img)
out = open("...\img.jpg", "wb")
out.write(p.content)
out.close()
