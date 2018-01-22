# 有四个新任务即将开放，你不应该需要超过一天的时间来完成他们。
# 所有这些任务都可以靠蛮力来完成，但是这并不是最好的办法。
# （你可能还没有进入这些新任务，他们即将开放在地图上的更多岛屿上）
#
# 这个任务是这个系列中的第一个。
# 在这里你应该找到字符串中最长的相同字符重复出现的次数，
# 并返回它的重复次数。
# 例如：字符串“aaabbcaaaa”包含具有相同字母
# “aaa”，“bb”，“c”和“aaaa”的四个子字符串。
# 最后一个子字符串是最长的一个字符串，你应该返回 4 。
#
# 输入: 一个字符串.
#
# 输出: 一个整数.

# long_repeat('sdsffffse') == 4
# long_repeat('ddvvrwwwrggg') == 3

import re


def long_repeat(line):
    x = []
    s = set(line)
    while len(s):
        b = s.pop()
        reg = re.compile('{}+'.format(b))
        x+=(reg.findall(line))
    return max([len(y) for y in x])

#
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-test
#     assert long_repeat('sdsffffse') == 4, "First"
#     assert long_repeat('ddvvrwwwrggg') == 3, "Second"
#     assert long_repeat('') == 0, "third"
#
#     print('"Run" is good. How is "Check"?')
