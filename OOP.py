class Person:
    counter = 0
    objects = list()
    
    def __init__(self, first_name: str, last_name: str, age=1):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.counter += 1
        Person.objects.append(self)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def is_teenage(self):
        return 10 < self.age < 20

    def introduce(self):
        print(f"Hi, I am {self.get_fullname()}")
        print(f"I am {self.age} years old")

    @classmethod
    def get_persons(cls):
        for person in cls.objects:
            print(person.get_fullname())

    @staticmethod
    def retirement_age():
        return 50


person_1 = Person("David", "Doe", 15)
# person_2 = Person("John", "Robinson", 2)

# person_1.introduce()
# person_2.introduce()
# print(Person.counter)
# print(Person.retirement_age())
print(Person.get_persons())