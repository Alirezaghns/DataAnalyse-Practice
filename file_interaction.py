Reading data
Writing data
Appending data

read(), readline(), readlines()
file_name = "/home/alireza/Codes/Python/Sample/textual_data/my_data.txt"
file_object = open(file_name, "r")

content = file_object.readlines()
for index, line in enumerate(content, 1):
    line = line.replace('\n', '')
    print(f"{index}. {line}")

file_object.close()

write(), writelines()
file_object = open("./new_data.txt", "w")

file_object.write("And this is the second")
lines = (
    "This is the first line\n",
    "This is the second line\n",
    "This is the third line\n"
)
file_object.writelines(lines)

file_object.close()

write(), writelines()
file_object = open("./new_data.txt", 'a')

file_object.write("This content is being appended\n")
file_object.writelines(['penultimate line\n', 'ultimate line\n'])

file_object.close()


import os
print(os.getcwd())
print(os.path.abspath("../../"))
print(os.path.basename("/home/alireza/Codes/Python/Sample/textual_data/my_data.txt"))

import json

file_object = open("my_data.json", "r")

content = file_object.read()
json_content = json.loads(content)
print(json_content['teamate']['is_student'])

file_object.close()

file_object = open("./textual_data/new_json_value.json", "w")

data = {
    "full_name": "Alireza Mortezae",
    "email": "alirezamortezaei50@gmail.com",
    "is_student": True,
    "level": "Silver",
}
json_content = json.dumps(data)
file_object.write(json_content)

file_object.close()


file_object = open("my_data.json", "r")

content = file_object.read()
json_content = json.loads(content)

json_content["first_name"] = json_content["first_name"].upper()
json_content["last_name"] = json_content["last_name"].upper()
file_object.close()

file_object = open("my_data.json", 'w')

content = json.dumps(json_content)
file_object.write(content)

file_object.close()

Camma separated value
import csv
file_object = open("data.csv", "r")

reader = csv.reader(file_object)
reader = csv.DictReader(file_object)
for data in reader:
    print(data['first_name'])

file_object.close()


import csv

file_object = open("./new_csv_data.csv", "w")

field_names = ["first_name", "last_name", "age"]
writer = csv.DictWriter(file_object, fieldnames=field_names)

writer.writeheader()
writer.writerow({"first_name": "Alireza", "last_name": "Mortezaei", "age": 23})
writer.writerow({"first_name": "David", "last_name": "Doe", "age": 45})

file_object.close()

import shutil
shutil.copy("./new_csv_data.csv", "./textual_data/new_2.csv")
shutil.move("./my_data.json", "./textual_data/new_2.json")
import os
os.remove("new_csv_data.csv")

file_object = open("./new_csv_data.csv", "w")
import json
with open("./textual_data/new_json_value.json", "r") as file_object:
    content = file_object.read()
    json_content = json.loads(content)
    print(json_content)

print(file_object.closed)