# def sum(num):
#     print(num)
#     if num == 0:
#         return 0
#     return num+sum(num-1)
# result = sum(5)
# print(result)

def factorial(num):
    print(num)
    if num == 1:
        return 1
    return num*factorial(num-1)


result = factorial(5)
print(result)