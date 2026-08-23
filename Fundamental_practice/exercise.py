#  Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];
# const array2 = ['z', 'y', 'x'];
# should return true.

#  2 parameters - arrays - no size limit
#  return true or false

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']


# def common_item(array, array2):
#     for letter in array:
#         for letter2 in array2:
#             if (letter == letter2):
#                 return True
#     else: 
#         return False

# result = common_item(array1, array2)
# print(result)


def common_item(array1, array2):
    storage1 = {}
    for letter in array1:
        storage1[letter] = True

    for letter2 in array2:
        if letter2 in storage1:
            return True
    
    return False

result = common_item(array1, array2)
print(result)