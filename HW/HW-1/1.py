#first soloutin
sentece = input('pleas enter your sentence : ')
sentece_parts = sentece.split()
joined_sentence = ' '.join(sentece_parts[::-1])
print(joined_sentence)


 #second soloution
sentence = input('pleas enter your sentence : ')
words = sentence.split()
result = []
for i in range(len(words) - 1, -1, -1):
    result.append(words[i])

print(' '.join(result))
