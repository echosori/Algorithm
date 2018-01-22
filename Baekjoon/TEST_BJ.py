import random

# A = [random.randint(0,100) for i in range(100)]
# print(A)


# N, X = map(lambda x: int(x), input().split())
# A = map(lambda x: int(x), input().split())
# a = ' '.join(map(str,[i for i in A if i<X]))
# print(a)

# 1546평균
# a = map(int, input())
# b = list(map(int, input().split()))
# c = list(map(lambda x: x / max(b) * 100, b))
# print(sum(c) / len(b))

# import re
#
# n = input()
# pt = re.compile("[A-Za-z'`]+")
#
# a = pt.findall(n)
# print(len(a))


# 2577숫자의 개수

# a = int(input())
# b = int(input())
# c = int(input())
#
# result = str(a * b * c)
# # print(result)
# k = [str(x) for x in range(0,10)]
# # print(k)
#
# for i in k:
#     print(result.count(i))


# OOXXOXXOOO
# import re
#
#
# def plus(n):
#     k = 0
#     while n > 0:
#         k += n
#         n -= 1
#     return k
#
#
# PT = re.compile("O+")
# n = int(input())
# for i in range(n):
#     G = PT.findall(input())
#     print(sum([plus(len(h)) for h in G]))


# n = input()
# ascending = "1 2 3 4 5 6 7 8"
# descending = "8 7 6 5 4 3 2 1"
#
# if n ==ascending:
#     print("ascending")
# elif n ==descending:
#     print("descending")
# else: print("mixed")

# 40점이상일때
# a = [int(input()) for i in range(5)]
# b = [i if i>40 else 40 for i in a ]
# print(int(sum(b)/5))

# # 아스크 전화
# n = input()
# print(ord(n))


# 알파벳 찾기
# import string
# n = input()
# a = string.ascii_lowercase
# b = [str(n.index(i)) if i in n else '-1' for i in a]
# print(' '.join(b))


# n = int(input())
# for i in range(n):
#     a,b = input().split()
#     a= int(a)
#     c = ''
#     for k in b:
#         c=c+k*a
#     print(c)

# import string
#
# n = input().upper()
# k = string.ascii_uppercase
# # print(k)
# a = [(i, n.count(i)) for i in k]
# # print(a)
# a.sort(key=lambda i: i[1], reverse=True)
# # print(a)
# # print(a)
# if a[0][1] == a[1][1]:
#     print('?')
# else:
#     print(a[0][0])


# 그룹단어 체크
# import re
# import string
#
# d = int(input())
# g = 0
# for j in range(d):
#     k = string.ascii_lowercase
#     n = input()
#     b = []
#     for i in k:
#         PT = re.compile("[{}]+".format(i))
#         a = PT.findall(n)
#         b.append(len(a))
#     if max(b) == 1:
#         g += 1
#     b.clear()
# print(g)
#


# 수자를 꺼꾸로
# def rev(s):
#     s = list(s)
#     s = reversed(s)
#     return int(''.join(list(s)))
#
# #
# a = max(list(map(rev,input().split())))
# print(a)
# count = int(input())
# z = 1
# while count > 0:
#     x, y = map(int, input().split())
#     # if x == y == 0:
#     #     break
#     print('Case #{}: {} + {} = {}'.format(z, x, y, x + y))
#     count -= 1
#     z += 1
#
# a = [1,2,3]
# a.insert(0,' ')
# print(a)12312312
