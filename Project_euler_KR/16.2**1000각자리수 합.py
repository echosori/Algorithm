# 215 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.
#
# 21000의 각 자리수를 모두 더하면 얼마입니까?

def sum(num):
    num = list(str(num))
    x = 0
    for i in num:
        x+=int(i)
    return x
print(sum(2**1000))
