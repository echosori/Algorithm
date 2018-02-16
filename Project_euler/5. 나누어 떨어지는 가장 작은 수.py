# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
#
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?


from functools import reduce

gcd = lambda a, b: (gcd(b, a % b) if a % b else b)

lcm = lambda a, b: a * b / gcd(a, b)

x = reduce(lambda x, y: lcm(x, y), range(1, 20))

print(x)

# fibonacci_cache = {}
#
# @lru_cache()
# def fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n - 1) + fibonacci(n - 2)
#     fibonacci_cache[n] = value
#     print(fibonacci_cache)
#
#     return value
#
#
# print(fibonacci(10))
