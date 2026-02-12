list_of_numbers = []              

for i in range(10):
    number = int(input(f'Enter integer #{i+1}: '))
    list_of_numbers.append(number)   

sum_of_even = 0
for number in list_of_numbers:
    if number % 2 == 0:
        sum_of_even += number

print("Sum of even numbers:", sum_of_even)

    