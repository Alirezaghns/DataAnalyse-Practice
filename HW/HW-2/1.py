while True:
    try:
        user_input = input('Please enter a non-negative integer: ')
        n = int(user_input) 
        
        if n < 0:
            raise ValueError('negative number')  
        
        break  

    except ValueError as e:
        if str(e) == 'negative number':
            print(' Number cannot be negative.')
        else:
            print('You must enter digits only.')

a, b = 0, 1
x = []

for _ in range(n):
    x.append(a)
    a, b = b, a + b

print(','.join(map(str, x)))
