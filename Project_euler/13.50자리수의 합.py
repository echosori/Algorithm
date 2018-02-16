with open('13.50자리수의 합') as f:
    sum = 0
    for i in f:
        sum+=int(i)

print(str(sum)[:10])
