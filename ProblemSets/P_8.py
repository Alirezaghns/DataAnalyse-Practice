def word_check(text):
    words = text.split()
    nice_words = list()

    for word in words:
        bad_chars = 0
        for char in word:
            if not char.isalpha():
                bad_chars += 1
                word = word.replace(char, "")
        
        if not bad_chars >= (len(word) + bad_chars) / 2:
            nice_words.append(word)
        
    final_string = ' '.join(nice_words)
    final_string = final_string.title()

    response_dict = dict()
    for word in final_string.split():
        if word in response_dict.keys():
            response_dict[word] += 1
        else:
            response_dict[word] = 1
    
    response_dict = dict(sorted(response_dict.items()))
    return response_dict


print(word_check("hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"))