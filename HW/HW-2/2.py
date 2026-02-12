def validate_national_code(code: str):
    try:
        
        if len(code) != 10:
            return False
        if len(set(code)) == 1:
            return False
        digits = []
        for ch in code:
            digits.append(int(ch))   
            
        s = 0
        for i in range(9):
            s += digits[i] * (10 - i)

        r = s % 11

        
        if r < 2:
            expected_control = r
        else:
            expected_control = 11 - r

        return digits[9] == expected_control

    except ValueError:
        return False
while True:
    user_input = input("enter your national code pleas ").strip()
    if user_input.lower() in ('exit', 'quit' ):
        print("exit the program")
        break
    
    if validate_national_code(user_input):
        print(f"valid national code ")
    else:
        print(f"not valid")

#2

# def validate_national_code(code: str) :
    
#     if len(code) != 10 or not code.isdigit():
#         return False
    
#     digits = []
#     for ch in user_input:
#         digits.append(int(ch))
    
#     s = 0
#     for i in range(9):
#         s += digits[i] * (10 - i)
    
#     r = s % 11
    
#     if r < 2:
#         expected_control = r
#     else:
#         expected_control = 11 - r
    
#     return digits[9] == expected_control

# while True:
#     user_input = input("enter your national code pleas ").strip()
#     if user_input.lower() in ('exit', 'quit', ):
#         print("exit the program")
#         break
    
#     if validate_national_code(user_input):
#         print(f"valid national code ")
#     else:
#         print(f"not valid")


