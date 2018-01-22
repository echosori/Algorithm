# 프로그램 명: paintblock
# 제한시간: 1 초
# 크기가 1*1*1 인 정육면체를 가지고 가로 A 세로 B 높이 C 인 직육면체를 만든 후 A×B×C (2≤A,B,C≤120)의 블록 겉면에 페인트를 칠하였다.
#
# 아래의 그림은 3x3x3 인 경우의 보기이다.
#
#
#
# 이 때 2 개의 면만 페인트가 칠해진 블록의 개수를 구하는게 문제이다. (블록은 직육면체이다)
#
# 입력
#
# A , B , C 가 차례대로 입력된다. A 는 가로, B 는 세로, C 는 높이이다.
# 출력
#
# 2개의 면만 페인트가 칠해진 블록의 개수를 첫째 줄에 출력한다.
# 입출력 예
#
# 입력
#
# 3 3 3
#
# 출력
#
# 12
# 출처:tncks0121(박수찬)


# 크기가 1x1x1인 큐브로 만든
# AxBxC( 가로x세로x높이 )인 직육면체를 만든 후,
# 그 직육면체의 겉면에 페인트를 칠했을 때
# 6면중 2면에만 페인트가 칠해진 큐브 개수를 찾는거,,,


print(sum(map(lambda x:(x-2)*4,(int(x) for x in input().split()))))