class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if not self.left:
                self.left = BinarySearchTree(new_value)
            else:
                self.left.insert(new_value)
        elif new_value > self.value:
            if not self.right:
                self.right = BinarySearchTree(new_value)
            else:
                self.right.insert(new_value)
    
    def display(self, level=0):
        if self.right:
            self.right.display(level + 1)
        print(" " * level * 4 + str(self.value))
        if self.left:
            self.left.display(level + 1)


root = BinarySearchTree(10)
root.insert(8)
root.insert(12)
root.insert(11)
root.insert(9)
root.insert(14)
root.display()