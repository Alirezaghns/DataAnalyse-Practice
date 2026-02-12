# number = input("Enter a number: ")

# while not number.isdigit():
#     number = input("Enter a number, not a character: ")

# number = int(number)
# for _ in range(number):
#     print("Hello World")

# --------------------------------- Exceptions
# ZeroDivisionError
# result = 10 / 0
# print(result)

# ValueError
# int_value = int("abc")

# TypeError
# result = "3" + 3
# print(result)
# name = "David"
# name()

# SyntaxError
# if 1 print("Hello World")

# NameError
# print(first_name)

# KeyError
# name = {
#     "first_name": "David",
#     "last_name": "Doe"
# }
# print(name["age"])

# IndexError
# emails = ["admin@gmial.com", "user@gmail.com"]
# print(emails[8])

# ImportError
# from my_package import calculator

# IndentError
# if 1 > 10:
# print("Yes its greater")

# ---------------------------------------- Handling errors
# while True:
#     try:
#         number = int(input("Enter a number: "))
#     except:
#         print("An error occured")
#         continue
#     break

# for _ in range(number):
#     print("Hello World")

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except ValueError as error_message:
#     print("Value error occured: ", str(error_message))
# except ZeroDivisionError:
#     print("ZeroDivisionError occured")
# else:
#     print("No error found")
# finally:
#     print("Done")

# ---------------------------------- Raising exceptions
# number = int(input("Enter a number: "))

# if number % 10 == 0:
#     raise ValueError("Input value must not be a coefficient of 10")

# print("A valid input")

# class TenCoefficientError(Exception):
#     def __init__(self, message, *args, **kwargs):
#         super().__init__(message, *args, **kwargs)

# number = int(input("Enter a number: "))
# if number % 10 == 0:
#     raise TenCoefficientError("Invalid input")

# try:
#     ...
# except:
#     ...