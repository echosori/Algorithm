import requests
from urllib import request
import re
count = 0
cache = {}
number = 12345
for i in range(400):
    link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(number)
    response = request.urlopen(link)
    text = response.get_text()
    try:
        number = re.findall("\d+", text)[-1]

    except IndexError:
        number = int(number) / 2
    # except IndexError:
    #     pass
    cache[count] =(text, number)
    print(count,text, number)
    count +=1

print(cache)
print(cache[398])
print(cache[399])
print(cache[400])
