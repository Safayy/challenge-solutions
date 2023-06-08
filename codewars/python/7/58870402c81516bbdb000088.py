def strings_construction(a, b):
    quantity = 0
    word = a        
    isLastLetterMatchFound = True
    while isLastLetterMatchFound and b != '':
        for l in word:
            for b_letter in b:
                if l == b_letter: #if a matching character is found, remove it from both strings
                    b = b.replace(l,'',1)
                    word = word.replace(l,'',1)
                    isLastLetterMatchFound = True
                    # print(f"{b_letter}\t{l}\t{b}\t{word}")
                    break
                else:
                    isLastLetterMatchFound = False
            if word == '': #reset word
                quantity += 1
                word = a
    return quantity

print( strings_construction("hnccv","hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn") )