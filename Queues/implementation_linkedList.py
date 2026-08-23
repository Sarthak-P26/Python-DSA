class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if not self.first:
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if not self.first :
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node 
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        main_node = self.first
        self.first = self.first.next
        self.length -= 1
        return main_node

    def printqueue(self):
        if not self.last:
            print("Queue is empty")
            return None

        array = []
        main_node = self.first
        while main_node :
            array.append(main_node)
            main_node = main_node.next

        return array
            

        