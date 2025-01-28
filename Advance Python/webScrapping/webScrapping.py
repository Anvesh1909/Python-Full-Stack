import re
import urllib
import urllib.request

web = ['https://www.amazon.in']

for i in web:
    obj1 = urllib.request.urlopen(i)
    obj2 = obj1.read()
    obj3 = re.findall("<title>.*</title>",str(obj2),re.I)
    print(obj3[0])



