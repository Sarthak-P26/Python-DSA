array = ["Sarthak", "Siddhi", "Anita", "Sangita", "Nemo"]


def printFirstItemThenFirstHalfThenSayHi100Times(array):
    print(array[0])

    middle_index = int(len(array)/ 2)
    for item in range(middle_index):
        print(array[item])

    for item in range(100):
        print("Hi")

printFirstItemThenFirstHalfThenSayHi100Times(array)