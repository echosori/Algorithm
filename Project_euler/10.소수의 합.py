# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
#
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?


import math


def prime(n):
    # n이하의 모든 소수를 리스트로 반환
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_sum(x):
    y = 0
    for u in range(2, x):
        if prime(u):
            y += u
    return y



print(prime_sum(2000000))
