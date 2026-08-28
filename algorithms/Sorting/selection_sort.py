array = [10, 1, 8, 2, 7, 9]
def selection_sort(array):
    length = len(array)

    for i in range(length - 1):
        min_index = i           # min_index = to start comparing smallest item
        for j in range(i+1, length):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

result = selection_sort(array)
print(result)