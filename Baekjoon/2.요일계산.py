week = "MON, TUE, WED, THU, FRI, SAT, SUN".split(', ')
x, y = map(lambda x: int(x), input().split())
import datetime

a = datetime.date(2007, 1, 1)
b = datetime.date(2007, x, y)
c = b - a
print(week[c.days%7])
