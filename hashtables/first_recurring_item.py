#[2, 5, 1, 2, 3, 5, 1, 2, 4] = It should return 2
#[2, 1, 1, 2, 3, 5, 1, 2, 4] = It should return 1
#[2, 3, 4, 5] = It should return None
# seen = {}
#     for item in range(len(array)):
#         seen[item] = array[item]

def first_recurring_item(array):
    seen = {}
    indexs = 0
    for num in array:
        if num in seen:
            return num
        seen[num] = indexs
        indexs += 1

    return None

result = first_recurring_item([2, 5, 1, 1, 2, 3, 5, 1, 2, 4])
print(result)


