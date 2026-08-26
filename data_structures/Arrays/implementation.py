class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {} 

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift(index)
        return item

    def shift(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length -= 1

    def __str__(self):
        array = []
        for key, values in self.data.items():
            array.append(values)
        return str(array)

newArray = MyArray()
newArray.push("Hi")
newArray.push("You")
newArray.push("!")
newArray.push("are")
newArray.push("nice")
newArray.delete(2)
print(newArray)