# def checkio(a, b):
#     if a<b:
#         b,a = a,b
#
#     a = list(reversed(list(bin(a)[2:])))
#     b = list(reversed(list(bin(b)[2:])))
#
#     z_ab = tuple(zip(a, b))
#
#     n = 0
#     for x, y in z_ab:
#
#         if x == '1' and y == '1':
#             n = n + 0
#         elif x == '0' and y == '0':
#             n = n + 0
#         elif x != '1' or y != '1':
#             n = n + 1
#
#     n = n + a[len(b):].count('1')
#     return n



FORMAT = '{0:0>32b}'
print(type(FORMAT))

def checkio(n, m):
    n = FORMAT.format(n)
    print(n,len(n))

    m = FORMAT.format(m)

    return sum([1 for i, _ in enumerate(n) if n[i] != m[i]])






if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

