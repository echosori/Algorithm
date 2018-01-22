# 프로그램 명: coci_slatkisi
# 제한시간: 1 초
# 미르코는 사탕가게안에 있는 매우 많은 사탕을 샀다. 그는 항상 정확한 양을 지불하지 못해서 가게주인 아주머니와 협상을 했다. 미르코는 아주머니에게 본인이 가진 가장 작은 지폐를 말하고, 그녀는 그가 지불할 수 있는 가장 가까운 값을 "반올림"한다.
#
# 예를 들어보자. 만약 미르코가 최소 100쿠나 지폐를 가지고 있고 그가 150쿠나 어치의 사탕 사길 원한다면, 가게 주인은 200쿠나로 반올림할 것이다. 만약 그가 149쿠나 만큼 사길 원하면, 그녀는 100쿠나로 반올림할 것이다.
#
# 최근 미르코는 가게 주인이 그를 속이고 있다고 의심한다. 그는 당신에게 그를 도와줄 수 있는 프로그램을 작성하길 원한다.
#
# 그녀의 어머니는 1, 10, 100, ... , 1000000000 단위의 지폐만을 준다. 그는 반드시 10의 거듭제곱꼴의 지폐만을 가진다. 미르코는 지폐를 매우 많이 가지고 있다.
#
# 입력
#
# 첫번째 줄에는 사탕의 가격 C (0 ≤ C ≤ 1 000 000 000)와 미르코가 가진 최소 지폐의 단위 K가 주어진다. (10^K 이 최소 지폐이다.)
# 출력
#
# 미르코가 지불해야하는 반올림한 값을 출력한다.
# 입출력 보충
#
# 입력
#
# 184 1
#
# 출력
#
# 180
#
# 10^1 = 10 이 최소로 가진 단위이니 180 190 중 180 이 가까워서 답은 180
#
# 입력
#
# 182 2
#
# 출력
#
# 200
#
# 10^2= 100 이 최소로 가진 단위이니 100 과 200 중 200 이 가까워서  200
# Mirko buys a lot of candy in the candy shop. He cannot always pay the exact ammount so the shopkeeper and he have an agreement. He tells the shopkeeper the smallest bill he has, and she rounds his ammount to the nearest number he can pay.
# For example, if the smallest bill Mirko has is a hundred bill, and he wants to buy 150 Kunas of candy, the shopkeeper rounds his ammount to 200 Kunas. If he wants to buy 149 Kunas of candy, the shopkeeper rounds his ammount to 100 Kunas.
#
# Lately, Mirko suspects the shoopkeeper is trying to cheat him. He asked you to help him. Write a program that will help him.
#
# His mother only gives Mirko 1, 10, 100, 1 000, ... , 1 000 000 000 Kuna bills. He never has bills that are not powers of 10. The bills he does have, he has in large ammounts. Mirko buys a lot of candy in the candy shop. He cannot always pay the exact ammount so the shopkeeper and he have an agreement. He tells the shopkeeper the smallest bill he has, and she rounds his ammount to the nearest number he can pay.
#
# 입력
#
# The first and only line of input contains two integers, C (0 ≤ C ≤ 1 000 000 000), the price of candy Mirko is going to buy, and K (0 ≤ K ≤ 9), number of zeros on the smallest bill Mirko has.
# 출력
#
# The first and only line of output should contain one integer, C rounded to the nearest amount Mirko can pay.
# 입출력 예
#
#
# 입력
#
# 184 1
#
# 출력
#
# 180
#
# 입력
#
# 123450995 1
#
# 출력
#
# 123451000
#
# 입력
#
# 182 2
#
# 출력
#
# 200
# 출처: COCI 2009/2010 contest3 2/6
# 번역: Fate

candy,smallest=(int(n) for n in input().split())

smallest=10**smallest

print(round(candy/smallest)*smallest)

