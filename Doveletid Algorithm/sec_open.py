# 프로그램 명: sec(open)
# 제한시간: 1 초
# 초(second)가 입력으로 주어진다.
#
# 이 를 몇 날 몇 시간 몇 분 몇 초 인지를 변경하는 프로그램을 작성하시오.
#
# 입력
#
# 초(second)가 입력으로 주어진다. 10 000 000 이하의 정수 이다.
# 출력
#
# 4 개의 정수를 출력한다.
# 날 시 분 초
#
# 입출력 예
#
# 입력
#
# 70
#
# 출력
#
# 0 0 1 10

a=int(input())
minute=60
hour=60*minute
day=24*hour

print(
      a//day,
      a%day//hour,
      a%day%hour//minute,
      a%day%hour%minute
      )

