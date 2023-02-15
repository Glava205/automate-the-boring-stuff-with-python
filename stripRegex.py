import re

def strip(s, symbols=r"\s"):
     strip.r1 = re.compile("^[{}]+".format(symbols))
     strip.r2 = re.compile("[{}]+$".format(symbols))
     return re.sub(strip.r1, '', re.sub(strip.r2, '', s))

strip("\tsome\ntext \t")
