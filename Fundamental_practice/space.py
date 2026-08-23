def boooooo(n):
    for item in range(len(n)):
        print("booooo!!!")


boooooo([1,2,3,4,5])


def array_of_n_times(n):
    hi_array = []
    for item in range(len(n)):
        hi_array.append("hi")
    return hi_array

n = [1,2,3,4,5,6]

a = array_of_n_times(n)
print(a)