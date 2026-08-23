# 1) First way of doing reverse String
# string = "Hi how are you?"
# a = []
# for letter in string:
#     a.insert(0, letter)
# reverse_string = (''.join(a))
# print(reverse_string)

# 2) Second way of reversing a string
# string = 'Hi how are you?'
# reverse_string = string[::-1]
# print(reverse_string)

# 3) Third way of reversing a string
# string = 'Hi how are you?'
# array = []

# for letter in string:
#     array.append(letter)
# array.reverse()
# reverse_string = ''.join(array)
# print(reverse_string)


# 4) DSA Way no shortcuts
# def reverse_func(string):
#     array = list(string)

#     if not isinstance(string, str):
#         raise TypeError(f'Expect a string, but got {string} ')

    # if (type(string) != str or len(string) < 2 ):
     #     return 'hmm that is not good'

#     left = 0
#     right = len(array) - 1

#     while left < right:
#         array[left], array[right] = array[right], array[left]
#         left += 1
#         right -= 1

#     return ''.join(array)


# a = reverse_func("Hi how are you")
# print(a)

# 5) Video Way of reversing a string
# def reverse_str(string):
#     if not isinstance(string, str):
#         raise TypeError("Expect a string type, given input is not correct!!")

#     if not string:
#         raise ValueError("Entered a empty string enter a correct string")

#     storage_arr = []
#     total_items = len(string) - 1

#     for item in range(total_items, -1, -1):
#         storage_arr.append(string[item])

#     return ''.join(storage_arr)

# reverse_string = reverse_str("HI how are you")
# print(reverse_string)

# 6) Short way with methods
# def reverse_two(string):
#     return ''.join(reversed(string))

