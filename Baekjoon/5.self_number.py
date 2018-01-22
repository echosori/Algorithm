def d(n):
    # self+every position
    return n+sum(map(int,list(str(n))))

# print(d(100))
def self():
    a = [d(n) for n in range(1, 10001)]
    for i in range(1, 10001):
        if i not in a:
            print(i)

# self()

import string

a = string.ascii_uppercase
print(a)
