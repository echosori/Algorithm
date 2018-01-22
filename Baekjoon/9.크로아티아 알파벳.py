from bs4 import BeautifulSoup
import requests
#
# req = requests.get("https://www.acmicpc.net/problem/2941")
# html = req.text
# soup = BeautifulSoup(html,'html.parser')
# table = soup.find(class_='table table-bordered').findAll("td")
#
#
# t = [i.get_text() for i in table]
# print(t)
#
# a = ['č', 'c=', 'ć', 'c-', 'dž', 'dz=', 'ñ', 'd-', 'lj', 'lj', 'nj', 'nj', 'š', 's=', 'ž', 'z=']
# b = {a[i+1]:a[i] for i in range(0,len(a),2)}
# print(b)
#
#
# x = 'ljes=njak'
# c = b.keys()
# print(list(c))
import re

#
# for i in c:
#     PT = re.compile("({})+".format(i))
#     a = PT.findall(n)
#     print(i,a)
n = input()


def crotia(n):
    c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    list_ = []
    for i in c:
        if i in n:
            list_.append(n.count(i))
            b = n.replace(i, '')
            n = b

    return sum(list_) + len(n), list_


print(crotia(n))
