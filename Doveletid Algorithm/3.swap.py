# 프로그램 명: swap
# 제한시간: 1 초
# 두 정수를 입력으로 받아 수를 교환하는 프로그램을 작성하시오.
# 입력
#
# 두 정수가 입력으로 주어진다.
# 출력
#
# 두 정수를 바꾸어서 출력한다.
# 입출력 예
#
# 입력
#
# 10 20
#
# 출력
#
# 20 10
#
# 입력
#
# 5 1
#
# 출력
#
# 1 5

def swap(a=input()):
    print(int(a.split()[1]), int(a.split()[0]))
swap()