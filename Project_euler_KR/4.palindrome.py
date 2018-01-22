def check_six(n):
    if len(str(n))==6:
        return True
    else:
        return False

def check_same(n):
    if check_six(n)==True:
        if str(n)[5]==str(n)[0] and str(n)[4]==str(n)[1] and str(n)[3]==str(n)[2]:
            return True
        else:
            return False
    else:
        return False

h=[]
for i in range(100,1000):
    for k in range(100,1000):
        h.append(i*k)


print(max(list(filter(lambda x :check_same(x),h   ))))