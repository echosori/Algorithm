# 스테판과 소피아는 보안에 대한 개념이 없어서 항상 간단한 비밀번호를 사용합니다.
# 니콜라가 비밀번호의 보안수준을 체크하는 모듈을 만들 수 있게 도와주세요.
# 비밀번호가 충분히 강력하다고 할 수 있으려면,
#
# 비밀번호의 길이는 10보다 크거나 같아햐 하고,
# 1개 이상의 숫자, 1개 이상의 대문자,
# 1개 이상의 소문자를 포함하고 있어야 합니다.
# 비밀번호는 ASCII 로마자만을 포합합니다.
#
# 입력: 비밀번호 문자열(string, 파이썬2.7과의 호환을 위해 유니코드로 주어짐).
#
# 출력: 비밀번호가 안전한지 아닌지를 나타내는 진리값(boolean),
# 혹은 진리값으로 간주할 수 있는 아무 자료형.





def checkio(data):

    data=list(data)
    list1=[]
    for i in data:
        if i.isupper():
            list1.append('hasupper')
        elif i.islower():
            list1.append('haslower')
        elif i.isdigit():
            list1.append('hasdigit')

    if len(list1)==len(data) and len(list1)>=10 and set(list1)=={'hasupper','haslower','hasdigit'}:
        return True
    else:
        return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

