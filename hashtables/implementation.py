class HashTable:
    def __init__(self, size):
        self.data = [None]* size

    def __str__(self):
        return str(self.__dict__)

    def __hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash +(ord(key[i]) * i)) % len(self.data)
        return hash

    def set(self, key, value):
        address = self.__hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        

    def get(self, key):
        address = self.__hash(key)
        current_bucket = self.data[address]
        if(current_bucket):
            for item in range(len(current_bucket)):
                if current_bucket[item][0] == key:
                    return current_bucket[item][1]
        return None

    def keys(self):
        key_array = []
        for i in range(len(self.data)):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        key_array.append(self.data[i][j][0])
                else:
                    key_array.append(self.data[i][0][0])
        return key_array

    def values(self):
        values_array = []
        for i in range(len(self.data)):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array 
            

obj1 = HashTable(2)
obj1.set("Grapes", 10000)
obj1.set("apples", 500)
obj1.set("melon", 2)
obj1.set("grapes", 323)
print(obj1.keys())
