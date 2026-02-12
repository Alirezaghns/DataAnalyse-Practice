numbers = input('enter the number whith space :')
list_of_numbers = list(map(int,numbers.split()))
for number in list_of_numbers : 
    def is_prime(number):
        if number <= 1:
            return False
        if number == 2:
            return True
        for i in range(3 , int(number**.5)+1):
                if number % i == 0 :
                    return False
        return True
for number in list_of_numbers:
    if is_prime(number):
        print(f"{number}your number is prime ")
    else:
        print(f"{number}  your number is not prime")       