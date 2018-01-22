# 서로다른 플러그의 종류가 50가지나 된다면, 기기를 다루는 일은 어렵고,
# 기기는 매우 비쌀 것입니다. 하지만 기기의 단자가 표준화된다면,
# 많은 기업들이 기기를 디자인할 수 있게 되고,
# 경쟁을 통해 소비자에게 싼 가격으로 더 좋은 상품을 제공할 수 있게 될 것입니다.
# -- 빌 게이츠
#
# 비어있지 않은 정수의 리스트 X가 주어집니다.
# 이 미션의 목표는 리스트 X로부터 유일하지 않은 요소만으로 구성된 리스트를 반환하는 것입니다.
# 그러기 위해서는 유일하게 존재하는 요소(리스트에서 단 한번만 등장하는 요소)만을 제거해야합니다.
# 제를 풀 때, 리스트의 순서를 바꾸어서는 안됩니다. 예를 들면 리스트 [1, 2, 3, 1, 3]에서
# 1과 3은 유일하지 않은 요소입니다. 즉 결과는 [1, 3, 1, 3]이 됩니다.

#Your optional code here
#You can import some modules or create additional functions

def checkio(data):
    return [x for x in data if data.count(x)>1]

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"

