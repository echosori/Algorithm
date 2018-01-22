# -*- coding: utf-8 -*-


# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 숫자와 앞에서 구한 합의
# 가장 오른쪽 자리 숫자를 이어 붙이면 새로운 수를 만들 수 있다.
#
# 다음 예를 보자.
#
# 26부터 시작한다. 2+6 = 8이다. 새로운 숫자는 68이다. 6+8 = 14이다.
# 새로운 숫자는 84이다. 8+4 = 12이다. 새로운 숫자는 42이다. 4+2 = 6이다.
# 새로운 숫자는 26이다.
#
# 위의 예는 4번만에 원래 숫자로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
#
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
# strN = input()


def plus(strN):
    if len(strN) == 1:
        return int(strN)
    else:
        return int(strN[0]) + int(strN[1])


def new_strN(strN):
    return strN[-1] + str(plus(strN))[-1]


a = [new_strN(str(i)) for i in range(0, 100)]
b = []
for i in range(0, 100):
    if len(str(i)) == 1:
        b.append('0' + str(i))
    else:
        b.append(str(i))

# for i in range(10):
# #     print(a[i*10:i*10+10])
# for i in range(10):
#     print(b[i*10:i*10+10])

for i in range(0,100):
    k = str(i)
    shuru = k if len(k) > 1 else '0' + k
    # print(shuru)
    count = 1
    # print(b.index(shuru))
    new = a[b.index(shuru)]
    # print(new)

    while new != shuru:
        new = a[b.index(new)]
        count += 1
    print(i ,count)
