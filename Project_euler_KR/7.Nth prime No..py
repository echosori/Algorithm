# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
#
# 이 때 10,001번째의 소수를 구하세요.
import math
def check_prime(n):
    if n==1:
        return False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def n_th_prime(n):
    m=[]
    i=0
    while len(m)<n:
        i += 1
        if check_prime(i):
            m.append(i)
    return max(m)

print(n_th_prime(10001))


