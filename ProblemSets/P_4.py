def calculate_floor(changes):
    floor = 0
    for change in changes:
        if change == "U":
            floor += 1
        elif change == "D":
            floor -= 1
    return floor


print(calculate_floor("DDDD"))