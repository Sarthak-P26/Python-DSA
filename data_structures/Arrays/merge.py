# 1) Easiest method to merging sorted array and sorting them
# def merge_sort_arrays():
#     l1 = [0, 3, 4, 31]  
#     l2 = [4, 6, 30]
#     l3 = l1 + l2
#     return sorted(l3)

# result = merge_sort_arrays()
# print(result)


#2) DSA Way to solve in the interview
def merge_sort_array(l1, l2):
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise TypeError("Both input need to be list")

    if not l1:
        return l2
    if not l2:
        return l1 
    
    merge_list = []

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merge_list.append(l1[i])
            i += 1
        else:
            # If l2[j] is smaller, grab it and move j forward
            merge_list.append(l2[j]) 
            j += 1

    # Your cleanup lines here are brilliant and perfectly correct!
    return merge_list + l1[i:] + l2[j:]

l1 = [0, 3, 4, 31]
l2 = [4, 6, 30]
result = merge_sort_array(l1, l2)
print(result)
