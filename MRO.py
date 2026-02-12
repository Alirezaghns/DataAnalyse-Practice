# Method Resolution order
class A:
    def introduce(self):
        print("Hi I am A")


class B:
    def introduce(self):
        print("Hi I am B")


class C(A, B):
    def introduce(self):
        print("Hi I am C")


class D(C):
    pass

b = B()
print(isinstance(b, D))