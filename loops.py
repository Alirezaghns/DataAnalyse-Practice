# user_input = input("Enter a number: ")
# int_user_input = int(user_input)

# is_prime = True

# for number in range(2, int(int_user_input ** 0.5) + 1):
#     if not int_user_input % number:
#         is_prime = False
#         break

# if is_prime:
#     print("Your number is prime")
# else:
#     print("Your number is not prime")
    
    
#2
n = int(input("Enter a number: "))

if n <= 1:
    print("Your number is not prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Your number is not prime")
        break
    else:
        print("Your number is prime")

