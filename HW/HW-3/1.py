# class Animal:
#     def __init__(self, name, voice):
#         self.name = name
#         self.voice = voice

#     def __str__(self):
#         return f"{self.name} says : {self.voice}"


# class Dog(Animal):
#     def __init__(self):
#         super().__init__("Dog", "HAP HAP")


# class Cat(Animal):
#     def __init__(self):
#         super().__init__("Cat", "MIOOOOW")


# class Cow(Animal):
#     def __init__(self):
#         super().__init__("Cow", "MOWWW")


# class Bird(Animal):
#     def __init__(self):
#         super().__init__("Bird", "CHICK CHICK")


# class Elephant(Animal):
#     def __init__(self):
#         super().__init__("Elephant", "TRUMPET")

# animals = [
#     Dog(),
#     Cat(),
#     Cow(),
#     Bird(),
#     Elephant()
# ]

# for animal in animals:
#     print(animal)



#2 soloution


# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self._sound = sound 

#     @property
#     def sound(self):
#         return self._sound

#     def make_sound(self):
#         print(f"{self.name} says : {self.sound}")

# class Dog(Animal):
#     def __init__(self):
#         super().__init__("Dog", "HAP HAP")

# class Cat(Animal):
#     def __init__(self):
#         super().__init__("Cat", "MIOOOOW")

# class Cow(Animal):
#     def __init__(self):
#         super().__init__("Cow", "MOWWW")

# class Bird(Animal):
#     def __init__(self):
#         super().__init__("Bird", "CHICK CHICK")

# class Elephant(Animal):
#     def __init__(self):
#         super().__init__("Elephant", "TRUMPET")

# animals = [
#     Dog(),
#     Cat(),
#     Cow(),
#     Bird(),
#     Elephant()
# ]

# for animal in animals:
#       animal.make_sound()



# 3th best soloution 

class Animal:
    def __init__(self, name, sound):
    
        if not isinstance(name, str):
            raise TypeError("Animal name must be a string")

        if not name.strip():
            raise ValueError("Animal name cannot be empty")

        if not isinstance(sound, str):
            raise TypeError("Animal sound must be a string")

        if not sound.strip():
            raise ValueError("Animal sound cannot be empty")

        self.name = name
        self._sound = sound

    @property
    def sound(self):
        return self._sound

    def make_sound(self):
        print(f"{self.name} says: {self.sound}")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "HAP HAP")


class Cat(Animal):
    def __init__(self):
        super().__init__("Cat", "MIOOOOW")


class Cow(Animal):
    def __init__(self):
        super().__init__("Cow", "MOWWW")


class Lion(Animal):
    def __init__(self):
        super().__init__("Lion", "ROAAAR")


class Snake(Animal):
    def __init__(self):
        super().__init__("Snake", "SSSSSS")


def main():
    try:
        animals = [
            Dog(),
            Cat(),
            Cow(),
            Lion(),
            Snake()
        ]

        for animal in animals:
            animal.make_sound()

    except (TypeError, ValueError) as e:
        print(f" Input Error: {e}")

    except Exception as e:
        print(f" Unexpected Error: {e}")

    finally:
        print(" Program finished successfully")


main()


