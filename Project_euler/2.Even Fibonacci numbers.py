# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

cache = {}
c = []
b = []
def fibo(n):
    if n in cache:
        b.append(1)
        return cache[n]
    elif n == 1 or n == 2:
        value = 1
        c.append(1)
    elif n > 2:
        value = fibo(n - 1) + fibo(n - 2)
        c.append(1)
    cache[n] = value
    return value


print(fibo(10))
print(cache)
print(len(c))
print(len(b))

#
# c = []
# def f(n):
#     c.append(1)
#     if n ==1 or n==2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# print(f(10))
# print(len(c))