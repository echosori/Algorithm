arr = [7, 3, 6, 8, 3, 2, 10, 28, 17, 2, 82]


def findsmallest(li):
    smallest = li[0]
    smallest_index = 0
    for i in range(1, len(li)):
        if li[i] < smallest:
            smallest = li[i]
            smallest_index = i
    return smallest_index


print(findsmallest(arr))

def sorted_arr(a):
    new_arr = []
    while a:
        new_arr.append(a.pop(findsmallest(a)))
    return new_arr

print(sorted_arr(arr))
print(len(arr))
print(len(sorted_arr(arr)))
