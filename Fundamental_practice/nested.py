array = [1,2,3,4,5]

def print_all_numbers_then_all_pair_sum(array):
    print("These are the numbers: ")
    for item in array:
        print(item)


    # for item in range(len(array)):
    #     for item2 in range(len(array)):
    #         print(array[item] + array[item2])
    print("These are the sums: ")
    for item in array:
        for item2 in array:
            print(item + item2)

print_all_numbers_then_all_pair_sum(array)
