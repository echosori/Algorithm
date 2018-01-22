# factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


# #
# # print(factorial(10))
#
# # generator
#
# def gen_factorail(x):
#     for i in range(x,0,-1):
#         yield i
# #
# # for i in range(10):
# #     print(next(gen))
#
# s = 'hellp world'
# gen = gen_factorail(len(s))
#
# for i in range(len(s)):
#     print(s[next(gen)-1])


print(factorial(100))