s = input("enter a string: ")
alpha = 0
digit = 0
char = 0

for ch in s:
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digit += 1
    else:
        char += 1

print("alphabet =", alpha)
print("digit =", digit)
print("character =", char)



        