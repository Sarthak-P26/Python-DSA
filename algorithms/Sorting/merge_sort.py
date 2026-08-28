def merge(sorted_left_side, sorted_right_side):
    i = 0
    j = 0
    sorted_list = []
    # while len(sorted_left_side) != 0 and len(sorted_right_side) != 0:
    while len(sorted_left_side) > i and len(sorted_right_side) > j :
        if sorted_left_side[i] < sorted_right_side[j]:
            sorted_list.append(sorted_left_side[i])
            i+= 1
        else:
            sorted_list.append(sorted_right_side[j])
            j+= 1

    sorted_list.extend(sorted_left_side[i:])
    sorted_list.extend(sorted_right_side[j:])
    return sorted_list



def merge_sort(nums):
    # Base Case
    if len(nums) == 1:
        return nums

    middle = len(nums) // 2
    split_left_side = nums[:middle]
    split_right_side = nums[middle:]
    sorted_right_side = merge_sort(split_right_side)
    sorted_left_side = merge_sort(split_left_side)

    return merge(sorted_left_side, sorted_right_side)

array = [10, 1, 8, 2, 7, 9]
result = merge_sort(array)
print(result)