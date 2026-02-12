# def fruits(tuple_of_fruits):
#     response_dict = dict()
#     for fruit in tuple_of_fruits:
#         if fruit['shape'] == "sphere":
#             if 300 <= fruit['mass'] <= 600:
#                 if 100 <= fruit['volume'] <= 500:
#                     if fruit['name'] in response_dict.keys():
#                         response_dict[fruit['name']] += 1
#                     else:
#                         response_dict[fruit['name']] = 1
#     return response_dict


def fruits(tuple_of_fruits):
    response_dict = dict()
    for fruit in tuple_of_fruits:
        if fruit['shape'] != "sphere":
            continue
        if not (300 <= fruit['mass'] <= 600):
            continue
        if not (100 <= fruit['volume'] <= 500):
            continue

        if fruit['name'] in response_dict.keys():
            response_dict[fruit['name']] += 1
        else:
            response_dict[fruit['name']] = 1
    return response_dict



print(fruits((
    {"name": "apple", "shape": "sphere", "mass": 350, "volume": 120},
    {"name": "mango", "shape": "square", "mass": 150, "volume": 120},
    {"name": "lemon", "shape": "sphere", "mass": 300, "volume": 100},
    {"name": "apple", "shape": "sphere", "mass": 500, "volume": 250},
)))