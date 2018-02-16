import random

# li = [random.randrange(1,100) for i in range(10)]
li = [100, 100, 89, 72, 63]
# print(sum(li))
s = []
# small = li[-1]
# count = 0
while len(li) > 0:
    for i in range(len(li) - 2, -1, -1):
        if li[i] > li[-1]:
            print('\t')

            print('\t')

            print(li[-1], 'last of the list')
            print(li[i], "index {} the element who challenged".format(i))
            li[-1], li[i] = li[i], li[-1]
            print('\t')
            print(li[-1], 'real last')
            print("================================")

    s.append(li.pop())
    # print(s)
    # print(li)
print("================================")
print("================================")
print("================================")

print(s, 'final list')
# print(count)
