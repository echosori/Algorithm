# nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
# n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
#  n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
# 예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고,
#  3이라면 'no'을 리턴하면 됩니다.
# #
# import math
# import time
# def nextSqaure(n):
#     if n in range(1,4) or math.sqrt(n)!=int(math.sqrt(n)):
#         return 'no'
#     return (math.sqrt(n)+1)**2
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : {}".format(nextSqaure(144)));
#
#
# t0=time.time()
# nextSqaure(144)
# t1=time.time()
# print('time pass',t1-t0)

# def nextSqur(n):
#     from math import sqrt
#     return 'no' if sqrt(n)%1 else (sqrt(n)+1)**2
#
# nextSqur(144)

# no_continuous함수는 스트링 s를 매개변수로 입력받습니다.
#
# s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.
# 예를들어 다음과 같이 동작하면 됩니다.
#
# s가 '133303'이라면 ['1', '3', '0', '3']를 리턴
# s가 '47330'이라면 [4, 7, 3, 0]을 리턴


def no_continuous(s):
    # 함수를 완성하세요
    return []

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))