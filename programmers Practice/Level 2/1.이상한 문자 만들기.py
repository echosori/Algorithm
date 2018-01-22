# 이상한 문자만들기
# Level 2
# toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
# 문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로, 홀수번째 인덱스 문자는 소문자로 바꾼 문자열을 리턴하도록 함수를 완성하세요.
# 예를 들어 s가 "try hello world"라면 첫 번째 단어는 "TrY",
# 두 번째 단어는 "HeLlO", 세 번째 단어는 "WoRlD"로 바꿔 "TrY HeLlO WoRlD"를 리턴하면 됩니다.
#
# 주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.

def toWeirdCase(s):
    # 함수를 완성하세요
    a = s.split(' ')
    b=list(map(lambda x:list(x),a))
    for i in range(len(b)):
        for k in range(len(b[i])):
            if k%2==0:
                b[i][k]=b[i][k].upper()
            b[i][k] = b[i][k].lower()
    return ' '.join(list(map(lambda x:''.join(x),b)))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("tKeSek Xjql yOFE")));



# ================================================


def toWeirdCase(s):
    # 함수를 완성하세요
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")))


# ======================================================

#
# def toWeirdCase(s):
#     res = []
#     for x in s.split(' '):
#         word = ''
#         for i in range(len(x)):
#             c = x[i].upper() if i % 2 == 0 else x[i].lower()
#             word = word + c
#         res.append(word)
#     return ' '.join(res)
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : {}".format(toWeirdCase("try hello world")));


# ========================================================


def toWeirdCase(s):
    # 함수를 완성하세요
    weird_case_li = [''.join([x[i].upper() if i % 2 == 0 else x[i].lower()
                    for i in range(len(x))]) for x in s.split(" ")]
    return ' '.join(weird_case_li)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));