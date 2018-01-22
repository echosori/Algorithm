a = 499


def checkio(a):
    k = [1, 5, 10, 50, 100, 500, 1000]

    data = []

    def check(a):
        for i in range(len(k)):
            if a >= 1000:
                return 1000
            if k[i] < a < k[i + 1]:
                return k[i]

    while a > 0:
        data.append((a // check(a), check(a)))
        a = a % check(a)

    return data


print(checkio(a))
#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     # assert checkio(6) == 'VI', '6'
#     assert checkio(76) == 'LXXVI', '76'
#     assert checkio(499) == 'CDXCIX', '499'
#     assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

# I	1 (unus)
# V	5 (quinque)
# X	10 (decem)
# L	50 (quinquaginta)
# C	100 (centum)
# D	500 (quingenti)
# M	1000 (mille)
