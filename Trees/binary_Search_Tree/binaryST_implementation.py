class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        current_node = self.root
        if not self.root:
            self.root = new_node
        else:
            while True:
                # duplicate handling
                if value == current_node.value:
                    return current_node
                # left
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        return new_node
                    else:
                        current_node = current_node.left
                #Right
                if value > current_node.value:
                    if not current_node.right:
                        current_node.right = new_node
                        return new_node
                    else:
                        current_node = current_node.right


    def lookup(self, value):
        current_node = self.root
        if not self.root:
            return False
        while True:
            if not current_node:
                return False
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
            elif value == current_node.value:
                return True

    def remove(self, value):
        current_node = self.root # previous Node
        previous_node = None # parent Node
        # Getting the Previous node and the node we want to remove
        while True:
            if not current_node:
                return None
            if value > current_node.value:
                previous_node = current_node
                current_node = current_node.right
            elif value < current_node.value:
                previous_node = current_node
                current_node = current_node.left
            else:
                break

        # For handling root condition
        if current_node.left ==None and current_node.right == None and previous_node ==None: # removing the main root node with no branches
                self.root = None

        elif current_node.left != None and current_node.right == None and previous_node == None: # if self.root only have a single left child
            self.root = current_node.left

        elif current_node.right != None and current_node.left ==None and previous_node == None:# if self.root only have a single right child 
            self.root = current_node.right


        # For leaf node with no left or right node
        elif current_node.left == None and current_node.right == None: # Check for leaf Node 

            if value > previous_node.value:
                previous_node.right = None
            else:
                previous_node.left = None

    # If the current Node one child only
        elif current_node.right != None and current_node.left ==None: # if the unwanted node have the child at right to make it the successor
            child_node = current_node.right

            if previous_node.right == current_node: 
                previous_node.right = child_node
            else:
                previous_node.left = child_node

        elif current_node.left != None and current_node.right ==None: # If the unwanted node have the child at left to make it the successor
            child_node = current_node.left

            if previous_node.right == current_node:
                previous_node.right = child_node
            else:
                previous_node.left = child_node

    # If the current Node have both left and right Node.
        else:
            unwanted_node = current_node
            parent = current_node
            current_node = current_node.right

            while current_node.left != None:
                parent = current_node
                current_node = current_node.left

            unwanted_node.value = current_node.value

            if parent == unwanted_node:
                parent.right = current_node.right
            else:
                parent.left = current_node.right
            






obj1 = Bst()
obj1.insert(9)
obj1.insert(4)
obj1.insert(1)
obj1.insert(6)
obj1.insert(20)
obj1.insert(15)
obj1.insert(170)
print(obj1)
