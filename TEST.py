# def powersum(power, *args):
#     '''Return the sum of each argument raised to the specified power.'''
#
#     total = 0
#     for i in args:
#         total += pow(i, power)
#     return total
#
#
# print(powersum(2, 3, 4))
# powersum(2, 10)

#
# a = [[(k,i) for i in range(5)] for k in range(5)]
# # for i in a:
# #     print(i)
# #     print('\b')
#
# a.reverse()
#
# for i in a:
#     i.reverse()
#     print(i)
# from tkinter import
# 在这个任务中，你应该自己写出PY3中实现的内建函数
# min
# 和
# max。 一些内建函数在这里是不能用的：import，eval，exec，globals。 别忘了，
# 你需要在你的代码中实现两个函数。
#
# max(iterable, *[, key])
# 或者
# min(iterable, *[, key])
# max(arg1, arg2, *args[, key]) 或者
# min(arg1, arg2, *args[, key])
#
# 返回迭代中的最大（最小）项中或者返回根据所提供参数的最大（最小）值 。
#
# 如果有一个参数时，它应该是一个迭代器。返回在迭代器的最大（最小）的项。如果提供两个或更多的参数，返回参数中的最大（最小）的项。
#
# 可选的唯一关键字是一个用于从每个列表元素提取一个用于比较的参数的函数。（例如，key = str.lower.lower）
#
# 如果有多个值同是最大（最小）的，函数返回所遇到的第一个最大值。
#
# -- Python
# 文档(内建函数)
#
# 输入: 一个参数作为一个迭代器或两个以上的参数。     一个函数作为可选关键字参数。
#
# 输出: "max"
# 函数输出最大的项
# "min"
# 函数输出最小的项。
#
# 范例:
#
# max(3, 2) == 3
# min(3, 2) == 2
# max([1, 2, 0, 3, 4]) == 4
# min("hello") == "e"
# max(2.2, 5.6, 5.9, key=int) == 5.6
# min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]

# 如何使用： 此任务将帮助你了解一些内置的功能是如何在
# 更精确的水平上工作的。
#
# 前提: 所有的测试用例都是正确的并且函数不会引发异常。

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    while i <= len(args):

    return None

#
# def max(*args, **kwargs):
#     key = kwargs.get("key", None)
#     return None


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

