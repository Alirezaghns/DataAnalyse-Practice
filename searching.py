def linear_search(numbers, value):
    for index, data in enumerate(numbers):
        if data == value:
            return index
    return -1

numbers = [4, 3, 2, 5, 1, 6, 4, 8]
value = 9
print(linear_search(numbers, value))

def binary_search(numbers, target_value):
    low, high= 0, len(numbers)-1

    while low <= high:
        middle = (low + high) // 2
        if numbers[middle] == target_value:
            return middle
        elif numbers[middle] < target_value:
            low = middle + 1
        else:
            high = middle - 1
    return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(numbers, 10))