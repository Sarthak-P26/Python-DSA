def find_factorial_iteratively(number):
    answer = 1
    for item in range(1, number+1):
        answer *= item
    print(answer)

find_factorial_iteratively(5)


def fibonacci_iterative(n):
    previous = 0
    current = 1

    for _ in range(n):
        next_number = previous + current
        previous = current
        current = next_number

    return previous

answer = fibonacci_iterative(6)
print(answer)  # 8