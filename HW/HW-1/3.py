fullname = input('Enter your full name : ')

parts = fullname.split()

if len(parts) >= 2:
    name = parts[0]
    lastname_parts = []

    for part in parts[1:]:
        lastname_parts.append(part)
        

    lastname =' '.join(lastname_parts)

    print(f"{lastname.upper()}@@{name.lower()}")
else:
    print("Please enter both a name and a last name.")

