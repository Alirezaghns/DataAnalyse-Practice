# def sum(first_number, second_number):
#     """ Adds two numbers and return the result """
#     return first_number + second_number


# def sub(first_number, second_number):
#     """ Subtracts two numbers and return the result """

#     return first_number - second_number

# def product(first_number, second_number):
#     """ Multiplies two numbers and return the result """
#     return first_number * second_number


# import math
# # from math import sqrt, pow

# result = math.sqrt(13)
# print(result)

# result = math.pow(2, 5)
# print(result)

# result = math.factorial(10)
# print(result)

# result = math.ceil(2.1)
# print(result)

# result = math.floor(2.9)
# print(result)

# result = math.pi
# print(result)

# ------------------------------- OS Module
# import os

# result = os.getcwd()
# print(result)

# result = os.listdir('.')
# print(result)

# result = os.mkdir("new_folder1")
# print(result)

# result = os.removedirs("new_folder1")
# print(result)

# result = os.remove("test.txt")
# print(result)


# ----------------------------------- Datetime Module

# import datetime

# result = datetime.date.today()
# print(result)

# result = datetime.date.now()
# result = result.date()
# result = result.time()
# result = (result + datetime.timedelta(hours=3)).time()
# print(result)

# result = datetime.datetime.strftime(result, "%H - %M - %S")

# ---------------------------------- Random Module
# import random

# result = random.randint(1, 10)
# print(result)

# ages = [23, 54, 13, 56, 67]
# result = random.choice(ages)
# print(result)

# random.shuffle(ages)
# print(ages)

# result = random.uniform(1, 10)
# print(result)

# ----------------------------- Numpy Module

import numpy as np

result = np.array([])
print(result)

result = np.zeros((10, 10))
print(result)

ages = [23, 54, 13, 56, 67]
result = np.mean(ages)
print(result)
result = np.var(ages)
print(result)
result = np.std(ages)
print(result)
