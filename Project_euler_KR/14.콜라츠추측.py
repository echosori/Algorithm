# 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.
#
# n → n / 2 (n이 짝수일 때)
# n → 3 n + 1 (n이 홀수일 때)
#
# 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도 마지막에는 1로 끝나리라 생각됩니다.
# (역주: 이것은 콜라츠 추측 Collatz Conjecture이라고 하며, 이런 수들을 우박수 hailstone sequence라 부르기도 합니다)
#
# 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 숫자는 얼마입니까?
#
# 참고: 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.

import time


def decorate(f):
    def wrapper(*args):
        start = time.time()
        result = f(*args)
        finish = time.time()
        print('함수 ' + f.__name__ + '의 실행 시간은 {}입니다'.format((finish - start) * 1000))
        return result

    return wrapper


#

def Collatz(num):
    count = 1
    while num > 1:
        if num % 2:
            num = 3 * num + 1
            count += 1
        else:
            num = num / 2
            count += 1
    return count


# list_ = []
# for i in range(1, 1000000 + 1):
#     list_.append((Collatz(i), i))

@decorate
def func(n):
    g = (Collatz(i) for i in range(1000000 + 1))
    i = 0
    k = 0
    while i < n + 1:
        a = next(g)
        if a > k:
            k = a
        i += 1
    return (k, i)


@decorate
def multi(x):
    return x * x ** x


print(func(100))
print(multi(232))
# print(max(list_))
# print('문제 풀이에 소요되는 시간은 [{:.2f}]초입니다.'.format(finish - start))
