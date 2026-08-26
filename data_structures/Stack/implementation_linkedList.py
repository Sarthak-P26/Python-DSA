# Singly Link List is used for implementing Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top == None:
            return None
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.bottom == None:
            self.bottom = new_node
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return self


    def pop(self):
        if self.top is None:
            return None

        pop_node = self.top
        self.top = self.top.next
        self.length -= 1

        if self.length == 0:
            self.bottom = None

        return pop_node

    def print_stack(self):
        if self.top is None and self.bottom is None:
            print("Stack is empty")
            return None

        array = []
        main_node = self.top

        while main_node is not None:
            array.append(main_node.value)
            main_node = main_node.next

        return array


obj1 = Stack()
obj1.push(1)
obj1.push(2)
obj1.push(3)
obj1.push(4)
obj1.push(5)
obj1.pop()
print(obj1.peek())
print(obj1.print_stack())