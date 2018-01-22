# 다음은 연속된 1000자리 숫자입니다 (읽기 좋게 50자리씩 잘라놓음).


# a = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

# 여기서 붉게 표시된 71112의 경우 7, 1, 1, 1, 2 각 숫자를 모두 곱하면 14가 됩니다.
#
# 이런 식으로 맨 처음 (7 × 3 × 1 × 6 × 7 = 882) 부터 맨 끝 (6 × 3 × 4 × 5 × 0 = 0) 까지 5자리 숫자들의 곱을 구할 수 있습니다.
# 이렇게 구할 수 있는 5자리 숫자의 곱 중에서 가장 큰 값은 얼마입니까?
import re
from functools import reduce

number = """731671765313306249192251196744265747423553491949969835203127745063262395783180169848018694788518858615607891129494954595017379583319528532088055125406987471585238630507156932909632952274430435668966489504452445231617318564030987111217223831622298934233803081353362766142828064444866452387303589072962904915604407723907138105158593079608701724271218839987979087922749219016997208880937657273330010533678812202354218097512545405947522525849077116705560136048395864467063244157221553536978179778461740649551492908625693219784686224839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""
# pattern = re.compile("\d{5}")
#
# m = re.findall(pattern, number)
#
# print(m)
#
#


# print(mm,mm.index(14), m[mm.index(14)])

m = []
for i in range(len(number)):
    if i + 5 <= len(number):
        m.append(number[i:i + 5])


def str_to_mul(a):
    a = list(a)
    b = list(map(lambda n: int(n), a))
    c = reduce(lambda x, y: x * y, b)
    return c


mm = list(map(lambda x: str_to_mul(x), m))

print(max(mm))