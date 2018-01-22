# 프로그램 명: coci_faktor
# 제한시간: 1 초
# [문제요약] 과학 논문 평가의 주요 요소는 다른 논문에 얼마나 많은 인용이 일어나는가가 주요 요소이다.
#
# 만약 38 개의 논문에 894 번의 인용이 일어났다면
#
# 평가 점수는 894/38 = 23.53
# 올림하면 24 이다.(항상 올림)
# y 개의 논문에 x 번의 인용이 일어난 경우 주요 요소 z 를 구할 수 있다. 문제는 y , z 가 주어질 때 최소 x 를 구하는 것이다.
#
# Impact factor of a scientific journal is a measure reflecting the average number of citations to articles published in science journals. For this task we are using a simplified formula for calculating the impact factor:
# Total sum of all citations articles published in the journal recived
# --------------------------------------------------------------------
#               Total number of articles published
# Rounding is always preformed up. For example the impact factor of the “Journal for ore research and time wasting” that published 38 articles quoted 894 times is 894 / 38 = 23.53 rounding up to 24.
# You are the editor of one scientific journal. You know how much article you are going to publish and the owners are pushing you to reach a specific impact factor. You are wondering how many scientists you will have to bribe to cite your article to meet the owners demands. Since money is tight you want to bribe the minimal amount of scientists.
#
# 입력
#
# First and only line of input will contain 2 integers, A (1 ≤ A ≤ 100), number of articles you plan to publish and I (1 ≤ I ≤ 100) impact factor the owners require.
# 출력
#
# First and only line of output should contain one integer, the minimal number of scientists you need to bribe.
# 입출력 예
#
# input
#
# 38 24
#
# output
#
# 875
#
# input
#
# 1 100
#
# output
#
# 100
#
# input
#
# 10 10
#
# output
#
# 91
# 출처:COCI 2009/2010 contest2 1/6
y,z=(int(n) for n in input().split())
print(y*(z-1)+1)