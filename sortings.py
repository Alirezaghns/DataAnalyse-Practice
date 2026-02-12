def bubble_sort(numbers):
    len_of_numbers = len(numbers)
    for i in range(len_of_numbers):
        for j in range(0, len_of_numbers - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


numbers = [4, 1, 2, 5, 3, 7, 3, 9]
sorted_list = bubble_sort(numbers)
print(sorted_list)


def selection_sort(numbers):
    len_of_numbers = len(numbers)

    for i in range(len_of_numbers):
        min_value = i
        for j in range(i+1, len_of_numbers):
            if numbers[j] < numbers[min_value]:
                min_value = j
        if min_value != i:
            numbers[i], numbers[min_value] = numbers[min_value], numbers[i]
    return numbers

numbers = [4, 3, 1, 5.0001, 7, 5, 4, 1, 2, 8]
sorted_list = selection_sort(numbers)
print(sorted_list)
