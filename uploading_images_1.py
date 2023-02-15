import urllib.request

with urllib.request.urlopen("...\img.jpg", 'wb') as our:
    out = open("...\img.jpg", 'wb')
    out.write(resource.read())
    out.close()
