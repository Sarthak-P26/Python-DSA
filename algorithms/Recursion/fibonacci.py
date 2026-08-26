def fibonacci_iterative(index): # My version after so much thinking
    array = [0, 1]

    for num in range(1, index):
        array.append(array[num] + array[num-1])


    return array[-1]

answer = fibonacci_iterative(6)
print(answer)


# GPT Way
def fibonacci_iterative_advance(index):
    previous = 0
    current = 1

    for _ in range(index):
        next = previous + current
        previous = current
        current = next

    return previous


def fibonacci_recursively(index):
    if index == 0:
        return 0
    if index == 1:
        return 1

    return fibonacci_recursively(index - 1) + fibonacci_recursively(index+1)