# N개의 최소공배수
# Level 3
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중
# 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다.
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중
# 공통이 되는 가장 작은 숫자가 됩니다. nlcm 함수를 통해 n개의 숫자가 입력되었을 때,
# 최소공배수를 반환해 주세요. 예를들어 [2,6,8,14] 가 입력된다면 168을 반환해 주면 됩니다.


# import random
# import math
#
# a = [random.randrange(50, 150) for i in range(5)]
# print(a)
#
# b = random.randrange(100)
# print(b)
#
import math
from functools import reduce
import random

def soyinsu(n):
    # n 은  정수 타입이다
    k = []
    i = 2
    while i < (int(math.sqrt(n)) + 1):
        if n % i == 0:
            k.append(i)
            n = n / i
        else:
            i += 1
    k.append(int(n))
    return k

def lcm_two(a, b):
    # a,b type is list
    c = []
    d = a + b
    if len(a) < len(b):
        a, b = b, a

    for i in set(d):

        if a.count(i) >= b.count(i):
            c.extend([i for x in range(a.count(i))])
        else:
            c.extend([i for x in range(b.count(i))])

    # print(c, 'c')
    lcm = reduce(lambda x, y: x * y, c)
    return lcm

# print(lcm_two([2,3],[3]))
# print(lcm_two([3],[2,3]))
def lcm(cc):
    i = 1
    x = cc[0]
    while i < len(cc):
        x = lcm_two(soyinsu(x), soyinsu(cc[i]))
        i += 1

    return x


print(lcm([2, 6, 8, 14]))
# print(x, 'x')
# print(lcm_two(soyinsu(24), soyinsu(14)), '24,14')
# print(soyinsu(24), soyinsu(14))

#
# print(lcm([2, 6, 8, 14]))
#
# print(lcm_two(soyinsu(2), soyinsu(6)), soyinsu(2), soyinsu(6))

# test if soyinsu() is OK.
# n = (random.randrange(1, 10000000000) for i in range(1, 10))
# for i in n:
#     if i == reduce(lambda x, y: x * y, soyinsu(i)):
#         print(i, soyinsu(i), True)
#         print(soyinsu(soyinsu(i)[-1]) if len(soyinsu(soyinsu(i)[-1]))==1
#               else 'Oh,it\'s a sad thing that you have wrong answer' )
#     else:
#         print('Oh,it\'s a sad thing that you have wrong answer')

# print(n)
# nn = soyinsu(n)
#
# print(soyinsu(n))
# print(reduce(lambda x, y: x * y, nn))

# [2, 2, 2, 3, 3]
# [2, 2, 2, 2, 2, 2]
# [2, 2, 2, 3]

# y = k.append(int(n))
# print(y)
# #
# def nlcm(num):
#     answer = 0
#
#     return answer
#
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(nlcm([2, 6, 8, 14]));
