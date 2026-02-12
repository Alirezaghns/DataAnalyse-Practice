# person = {"admin@gmial.com", "user@gmail.com"}
person = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@gmail.com",
    "age": 25,
    "address": {
        "city": "San Francisco",
        "street": "1st Street",
        "floor": "2nd Floor"
    }
}

# print(type(person))
# print(person['address']['city'])
#print(type(list((person.items()))))
# print(list(person.keys())[0])
# print(list(person.values())[-1])
# print(list(person.items())[0][1])

print(person.get("fullname", "No name"))

# print(person.pop("first_name"))
# print(person)

# person.update({"gender": "male"})
# print(person)

# print(person)
# person.clear()
# print(person)