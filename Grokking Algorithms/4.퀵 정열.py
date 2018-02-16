# 练习
#
# 4.1 请编写前述sum函数的代码。
#
# 4.2 编写一个递归函数来计算列表包含的元素数。
#
# 4.3 找出列表中最大的数字。
#
# 4.4 还记得第1章介绍的二分查找吗？它也是一种分而治之算法。
#     你能找出二分查找算法的基线条件和递归条件吗？
import time
import random
from functools import lru_cache


# @lru_cache()
# def plusAll(li, item):
#     if len(li) == 1:
#         if li[0] == item:
#             return 'Yes'
#         else:
#             return "don't have the candy you are searching"
#     low = 0
#     high = len(li) - 1
#
#     mid = (low + high) // 2
#
#     if item == li[mid]:
#         return mid
#     elif item > li[mid]:
#         low = mid + 1
#     elif item < li[mid]:
#         high = mid - 1
#     li = li[low:high]
#
#     # elif len(li) == 0:
#     #     return 1
#     return plusAll(li, item)
#
#
# a = [1,2,4,5,6]
#
# print(a)
#
# print(plusAll(a,2))

# print(a)
# print(plusAll(a))
# print(max(a))
#
#
# def find_smallest(li):
#     print(li)
#     smallest = li[0]
#     for i in range(1, len(li)):
#         if li[i] < smallest:
#             smallest = li[i]
#     return smallest
#
#
# print(find_smallest([random.randrange(1, 100) for i in range(10)]))
#
#
# def binary_search(li, item):
#     low = 0
#     high = len(li) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if item == li[mid]:
#             return mid
#         elif item > li[mid]:
#             low = mid + 1
#         elif item < li[mid]:
#             high = mid - 1
#     return "===  don't have this item  ==="
#
#
# a.sort()
# print(a)
# print(binary_search(a, 7

def quick_sort(li):
    if len(li) < 2:
        return li
    else:
        pivot = li[0]
        less = [i for i in li[1:] if i <= pivot]
        greater = [i for i in li[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


a = [random.randrange(100) for i in range(30)]
print(a)
print(quick_sort(a))
