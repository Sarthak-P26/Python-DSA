array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 40]

for i in range(1, len(array)):
    current = array[i]
    prev = i - 1

    while prev >= 0 and array[prev] > current:
        array[prev + 1] = array[prev]
        prev -= 1

    array[prev+1] = current