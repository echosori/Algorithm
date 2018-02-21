import string
import re
datum = ''.join(['j', 'f', 'e', 'i', 'a', 'u', 'z', 'r', 'o', 'i', 'v', 'g', 'z', 'b', 'm', 'p', 's', 'z', 'a', 'z', 'l', 'u', 't', 'n', 'w', 's', 'd', 'o', 'f', 'd', 'b', 'i', 'w', 'q', 'd', 'j', 'b', 'z', 's', 'h', 'f', 'r', 'b', 'l', 'q', 'g', 's', 'b', 'y', 'f', 'd', 'a', 'j', 'y', 'g', 'c', 'b', 'l', 'w', 'j', 'w', 'g', 'g', 't', 'd', 'f', 'j', 'e', 't', 'o', 'b', 'c', 'm', 'd', 'l', 'z', 'x', 'a', 'j', 'v', 'i', 't', 'h', 'e', 'c', 'g', 'p', 'k', 'c', 'f', 'w', 'q', 'q', 'b', 'v', 'k', 'o', 'i', 'e', 't', 'p', 'i', 'i', 'j', 'a', 'n', 'v', 'v', 'q', 'j', 'j', 'g', 't', 'c', 't', 'p', 'c', 'a', 'd', 'z', 'j', 'k', 'g', 'u', 'c', 'm', 'l', 'u', 'a', 'i', 'd', 'g', 'u', 'm', 'l', 'c', 'd', 's', 'k', 'u', 'n', 'u', 'j', 'f', 'c', 'j', 'f', 'm', 'b', 'z', 'k', 'z', 'x', 's', 'a', 's', 'd', 'x', 's', 'q', 'q', 'q', 'l', 'a', 'e', 'i', 's', 'j', 'e', 'f', 'j', 'f', 'd', 'a', 'o', 'l', 'k', 'j', 'a', 'k', 'y', 'p', 'w', 'x', 'j', 't', 'l', 'h', 'q', 'j', 'k', 'n', 'e', 'd', 'n', 'x', 'u', 'n', 's', 'a', 'h', 'x', 'q', 'e', 'd', 'o', 'e', 'q', 's', 'd', 'c', 'm', 'm', 'h', 'l', 't', 'c', 'q', 's', 'n', 'w', 'a', 'k', 'j', 'x', 't', 'e', 't', 'a', 'a', 'l', 'h', 'g', 'a', 'b', 'e', 'k', 'f', 'm', 'y', 'i', 'm', 'w', 'r', 'k', 'f', 'f', 'y', 'd', 'g', 'h', 'i', 'u', 'n', 'l', 'r', 'o', 'i', 'w', 'g', 'k', 'u', 'd', 'z', 's', 'q', 'l', 'j', 'j', 'b', 's', 'i', 'x', 'g', 'u', 'y', 't', 'f', 's', 'a', 't', 'e', 'j', 'm', 'd', 'w', 'k', 'f', 'b', 'z', 'i', 'f', 'd', 'k', 'n', 'p', 'a', 'c', 'q', 'i', 'm', 'v', 'e', 'h', 'x', 'u', 'j', 's', 'z', 'm', 'b', 'u', 'y', 'u', 't', 's', 'o', 'm', 'p', 'i', 'j', 'c', 'j', 'o', 'j', 's', 'p', 'b', 'y', 'w', 'l', 'r', 'o', 'e', 'f', 'i', 'w', 'm', 'r', 's', 'j', 's', 't', 'd', 'j', 'h', 'g', 'w', 'x', 'h', 'n', 't', 'h', 's', 'o', 'o', 's', 'm', 'o', 'q', 't', 'm', 'u', 'f', 'o', 'x', 'v', 'p', 'v', 'p', 'j', 'p', 'k', 'g', 'i', 'a', 'q', 'g', 'f', 'r', 'h', 'u', 'f', 'x', 'x', 'd', 'n', 'j', 'i', 'w', 't', 'f', 'q', 'u', 's', 'b', 'k', 'e', 'a', 'k', 'u', 'n', 'q', 'j', 'g', 'd', 'k', 'n', 'd', 'p', 'w', 'i', 'b', 'l', 'k', 'l', 'g', 'j', 'o', 'u', 'n', 'i', 'v', 'h', 'g', 'x', 's', 'n', 'e', 'k', 'x', 'j', 'g', 'r', 'r', 'b', 'n', 's', 'l', 'p', 'u', 'a', 'o', 'u', 'v', 'h', 'z', 'a', 'b', 'i', 'l', 'b', 'i', 'm', 'r', 'm', 'q', 'q', 'x', 't', 'k', 't', 'g', 'c', 'n', 'k', 'd', 'l', 'j', 'o', 'a', 's', 'h', 'n', 'e', 'k', 'x', 'w', 't', 's', 'g', 'v', 'z', 'w', 'j', 'a', 'e', 'h', 'g', 'u', 'r', 'n', 'k', 's', 'o', 'k', 'j', 't', 'r', 'o', 'v', 'p', 'm', 'y', 'g', 'k', 'z', 'g', 'e', 'o', 'l', 'w', 'y', 's', 'f', 'i', 'o', 'd', 'e', 'm', 'f', 'l', 'm', 'k', 'w', 'm', 'j'])
print(datum)
a = string.ascii_lowercase
pattern = re.compile("\W")
new_string = ''
x = datum
for i in x:
    if i in list(a):
        new_string += a[(a.index(i) + 2) % 26]
    elif re.match(pattern,i):
        new_string += i
print(x)
print(new_string)


# a = 'stringmaketrans'
# a = a.upper()
# print(a)

# # print(a)
# x = "!@#$%^&*()"
# y = '1234567890'
#
# import re
# p = re.compile("\w")
# k = re.findall(p,a)
# print(a)
#
# intab = x
# outtab = y
#
# transtab = str.maketrans(x,y)
# b = a.translate(transtab)
# print(b)
#
# p2 = re.compile(r"[\d]+")
#
# text = re.findall(p2,b)
# print(''.join(text))
# print(sum([int(i) for i in text]))
# print(text)