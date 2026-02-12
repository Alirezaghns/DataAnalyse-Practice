numbers = (input("enter number separated by space : "))
numbers_list = numbers.split()
joined_numbers = "*".join(numbers_list)
print(f"numbers with * : {joined_numbers}")