user_input = input("please enter a sentence : ")
first_five = user_input[: 5]
other = user_input[5 :]
reverse_five = first_five[: : -1]
print(reverse_five + other)