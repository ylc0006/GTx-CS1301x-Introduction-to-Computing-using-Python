def length_words(string):
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("'", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    string = string.lower()
    stringList = string.split()
    
    len_word_dict={}
    
    for word in stringList:
        wordLength = len(word)
        if not wordLength in len_word_dict:
            len_word_dict[wordLength]=[]
        len_word_dict[wordLength].append(word)
        
    return len_word_dict
        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))
