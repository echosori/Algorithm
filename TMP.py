from collections import deque

DQ = deque()
DQ += [1, 2, 3]
DQ += [5, 6, 7]

a = {'quan': 'hell', 'byonggchen': 'wuxi', 'longgnan': 'States'}
print(a)
print(a.items())
print(a.keys())
print(a.values())
print(a.get('quan'))
a.update({'lijian':'beijingg'})
a['dongyun'] = 'shenzhen'
print(a)