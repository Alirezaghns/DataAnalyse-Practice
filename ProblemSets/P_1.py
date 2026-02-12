def calculator(n, m, li):
    sub_lists = []
    extra = int(bool(n % m))
    for i in range(n // m + extra):
        sub_lists.append(sum(li[i*m:i*m+m]))
    
    total = 0
    for i in range(len(sub_lists)):
        if i % 2:
            total -= sub_lists[i]
        else:
            total += sub_lists[i]
    return total


print(calculator(12, 4, [5, 4, 2, 6, 8, 3, 5, 7, 5, 3, 2, 1]))