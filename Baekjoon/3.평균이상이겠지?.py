output_ = """40.000%
57.143%
33.333%
66.667%
55.556%"""

input_ = """5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91"""
#
#


case = int(input())
for i in range(case):
    a = list(map(int, input().split()))
    b = a[1:]
    average = sum(b) / a[0]
    more_than_average = [x for x in b if x > average]
    ratio = len(more_than_average) / len(b) * 100
    print('%0.3f' % ratio + '%')
# b = input().split('\n')
#
# c = (list(map(int, b[i].split())) for i in range(1, len(b)))
#
# for i in c:
#     d = [x for x in i[1:] if x > (sum(i[1:]) / len(i[1:]))]
#     # print(i[1:])
#     # print(d)
#     print('%0.3f' % ((len(d) / len(i[1:]) * 100)) + '%')
#
#
#     # print("%.3f%%" % round(rate, 3))
