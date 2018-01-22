# 등차수열

n = input()


def no(i):
    k = list(map(int, list(str(i))))
    if k[0] - k[1] == k[1] - k[2]:
        return True
    else:
        return False


def hansu(n):
    count = 0
    if n ==1000:
        n=999
    if n in range(1, 1000):
        for i in range(1, int(n) + 1):
            if i < 100:
                count += 1
            elif no(i):
                count += 1

        return count
    # elif n == 1000:
    #     pass


print(hansu(int(n)))
