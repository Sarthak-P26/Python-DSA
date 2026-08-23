# array = [1, 2, 4, 4] ; Sum = 8
# Output = Boolean (True/False)

def check_sum(array, sum):
    leng = len(array)
    for item in range(leng - 1):
        for element in range(item+1, leng):
            if array[item] + array[element] == sum:
                return True
    return False
