def binary_search(itme, li):
    low = 0
    high = len(li) - 1

    while low <= high:
        mid = (low + high) // 2
        if itme == li[mid]:
            return mid
        elif itme < li[mid]:
            high = mid - 1
        elif itme > li[mid]:
            low = mid + 1
    return 'don\'t have one in the list '


list_ = [i for i in range(1,100000+1)]
print(binary_search(30000000, list_))
print(list_[10])

print(binary_search.__name__)

import math

a = math.log(100,2)
print(a)
print(2**6)