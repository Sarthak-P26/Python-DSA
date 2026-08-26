class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        if not self.array:
            return None
        return self.array[-1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if not self.array:
            return None
        return self.array.pop()

    def print_stack(self):
        print(self.array)