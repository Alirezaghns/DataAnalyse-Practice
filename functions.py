def power(*args):
    return_value = list(map(lambda number: number ** 2, args))
    return return_value

numbers = input("Enter some values: ")
numbers = numbers.split()
numbers = list(map(lambda number: int(number), numbers))

final_value = power(*numbers)
print(*final_value, sep="\n")