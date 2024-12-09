def noof_letters(sent):

    count = 0
    for char in sent:
       
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            count += 1
    return count


sent = input("Enter any sentence: ")
print("The number of letters in the sentence is:", noof_letters(sent))
