# input_string = str(input())
# array = []
# for i in range(len(input_string)):
#     if (ord(input_string[i]) - 97) % 2 == 0:
#         array.append(input_string[i])
#     else:
#         array.append(input_string[i].upper())
# array.sort(reverse=True)
# answer = " ".join(array)
# print(answer)

# IF_RETURN if CONDITION else ELSE_RETURN

print(*sorted([i if (ord(i) - 97) % 2 == 0 else i.upper() for i in input()], reverse=True), sep=" ")
