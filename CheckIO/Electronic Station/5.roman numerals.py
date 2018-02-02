def make_roman(one, five, ten):
    li = []
    if five and ten:
        for i in range(0, 12):
            if i == 1:
                li.append(one)
            elif i > 1 and i < 4:
                li.append(one * i)
            elif i == 4:
                li.append(one + five)
            elif i == 5:
                li.append(five)
            elif i > 5 and i < 9:
                li.append(five + (one * (i - 5)))
            elif i == 9:
                li.append(one + ten)
            elif i == 10:
                li.append(ten)
            elif i == 11:
                li.append('')
    else:
        for i in range(1, 4):
            if i == 1:
                li.append(one)
            elif i > 1 and i < 4:
                li.append(one * i)
    return li


one = make_roman("I", "V", "X")
two = make_roman("X", "L", "C")
three = make_roman("C", "D", "M")
four = make_roman("M", None, None)
roman = [one, two, three, four]


def checkio(data):
    x = []

    data = list(str(data))
    data.reverse()
    for i in range(len(data)):
        x.append(roman[i][int(data[i]) - 1])

    x.reverse()
    x = ''.join(x)
    return x


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print("OK?Let us check it out")
# 罗马数字来源于古罗马编码系统。它们是基于字母表的特定字母的组合，
# 所表示的数等于这些数字相加（或者是相减）得到的数。前十位的罗马数字是：
#
# I，II，III，IV，V，VI，VII，VIII，IX和X。
#
# 罗马记数系统不是直接的十进制为基础，它没有零。
# 罗马数字是根据这七个符号的组合：
#
# 符号
# 值
# I
# 1(unus)
# V
# 5(quinque)
# X
# 10(decem)
# L
# 50(quinquaginta)
# C
# 100(centum)
# D
# 500(quingenti)
# M
# 1, 000(mille)
# 更多额外的关于罗马数字的信息可以参考
# 维基百科的文章.
#
# 在这个任务里，你应该返回给出指定的整数值的范围从1到3999的罗马数字。
#
# 输入: 一个整数(int).
#
# 输出: 一个字符串形式的罗马数字(str).
#
# 前提: 0 < number < 4000
