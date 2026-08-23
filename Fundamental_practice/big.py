from time import time

array = ["Sarthak", "Siddhi", "Anita", "Sangita", "Nemo"]
array2 = ["Sarthak", "Siddhi", "Anita", "Sangita"]

def findNemo(array):
    t0 = time()
    for item in array:
        print("running")
        if item == "Nemo":
            print("Nemo is founded")
            break
    else: 
        print("Nemo is not founded in the list")
    t1 = time()
    print("Time taken ", (t1 - t0))


findNemo(array)