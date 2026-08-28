array = [10, 1, 8, 2, 7, 9] # bubble Sort
array2 = ['a', 'z', 'j', 'b', 'k', 'c']
# def buble_sort(array):
#     b = len(array)
#     while b:
#         for i in range(b-1):
#             if array[i] > array[i+1]:
#                 #Swapping numbers
#                 array[i], array[i+1] = array[i+1], array[i]
#         b-=1
#     return array

# sorted_array = buble_sort(array)
# print(sorted_array)
 

def bubble_sort(array):
    b = len(array)
    while b: 
        swap = False
        for i in range(b-1):
                if array[i] > array[i+1]:
                    #Swapping numbers
                    array[i], array[i+1] = array[i+1], array[i]
                    swap = True
        b-=1
        if not swap:
             return array

result = bubble_sort(array)
print(result)