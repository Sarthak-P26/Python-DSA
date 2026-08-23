class LinkedList:

    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            "value": value,
            "next": None
        }

        print(new_node)

        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend(self, value):
        new_node = {
            "value": value,
            "next": None
        }

        new_node["next"] = self.head
        self.head = new_node
        self.length += 1

        return self

    def print_list(self):
        array = []

        current_node = self.head

        while current_node is not None:
            array.append(current_node["value"])
            current_node = current_node["next"]

        return print(array)

    def insert(self, index, value):

        # Check for proper parameters
        if index >= self.length:
            print("yes")
            return self.append(value)

        new_node = {
            "value": value,
            "next": None
        }

        leader = self.traverse_to_index(index - 1)
        holding_pointer = leader["next"]

        leader["next"] = new_node
        new_node["next"] = holding_pointer

        self.length += 1

        return self.print_list()

    def traverse_to_index(self, index):

        # Check parameters
        counter = 0
        current_node = self.head

        while counter != index:
            current_node = current_node["next"]
            counter += 1

        return current_node

    def remove(self, index):

        # Check parameters
        leader = self.traverse_to_index(index - 1)
        unwanted_node = leader["next"]

        leader["next"] = unwanted_node["next"]

        self.length -= 1

        return self.print_list()

    def reverse(self):

        if self.head["next"] is None:
            return self.head

        first = self.head
        second = first["next"]

        while second:
            temp = second["next"]
            second["next"] = first
            first = second
            second = temp

        self.head["next"] = None
        self.head = first

        return self.print_list()


my_linked_list = LinkedList(10)

my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)

my_linked_list.print_list()

my_linked_list.insert(2, 99)
my_linked_list.insert(20, 88)

my_linked_list.print_list()

my_linked_list.remove(2)

my_linked_list.reverse()