full_name = input("enter your first name and last name : ")
name_part = full_name.split()
first_name = name_part[0]
last_name = name_part[1]
print(f"first name : {first_name}")
print(f"last name : {last_name}")
joined_name = " ## ".join(name_part)
print(f"your new name is : {joined_name}")