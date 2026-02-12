sentence = input("Please enter the sentence: ").lower()
word = input("Please enter the word: ").lower()

index = sentence.find(word)

if index != -1:
    print(f"First occurrence is at index: {index}")
else:
    print("The word was not found.")
