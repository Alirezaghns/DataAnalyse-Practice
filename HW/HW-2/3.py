while True:
    try:
        user_input = input("enter the sentence: ") 
        
        if not user_input.strip():
            raise ValueError("Input cannot be empty")

        user_input = user_input.lower().strip()

        punctuations = ".,!?"   
        for p in punctuations:
            user_input = user_input.replace(p, "")
    
    
        words = user_input.split()
    
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    
        print(word_count)
        break
    except ValueError as e:
        print("Invalid input:", e)
