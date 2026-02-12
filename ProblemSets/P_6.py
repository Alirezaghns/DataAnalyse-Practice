# Handle in setter function
# class Foo:

#     def __init__(self):
#         self._x = 0

#     @property
#     def x(self):
#         return self._x
    
#     @x.setter
#     def x(self, value):
#         if value > 0:
#             self._x = value % 100
#         else:
#             self._x = -1

# Handle in getter function
class Foo:

    def __init__(self):
        self._x = 0

    @property
    def x(self):
        if self._x >= 0:
            return self._x % 100
        return -1
    
    @x.setter
    def x(self, value):
        self._x = value

obj = Foo()
print(obj.x)
obj.x = 342
print(obj.x)