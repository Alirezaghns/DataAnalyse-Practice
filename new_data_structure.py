emails = ["user@example.com"]
print(type(emails))

# Tuple
emails = ("user@example.com",)
print(type(emails))

ages = [12, 16, 23, 16, 9]
print(ages, type(ages))

ages = {12, 16, 23, 16, 9}
ages_2 = {35, 44, 16}

print(ages | ages_2)
print(ages & ages_2)
print(ages - ages_2)


emails = ["user@example.com", "admin@gmail.com"]
print(list(enumerate(emails)))