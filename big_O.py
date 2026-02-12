def find_sum(numbers):
    total = 0 # O(1)
    for num in numbers:
        total += num # O(n)
    return total # O(1)

print(find_sum([1, 4, 2, 3]))