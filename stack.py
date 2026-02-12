# LIFO
class Stack:
    def __init__(self):
        self.data = list()

    def push(self, value):
        """ Push a new item to the end of stack """
        self.data.append(value)
    
    def pop(self):
        """ Return the last item from stack """
        return self.data.pop()
    
    def peek(self):
        """ Visite the last item from stack """
        return self.data[-1]
    
my_stack = Stack()
my_stack.push(10)
my_stack.push(30)

print(my_stack.pop())
