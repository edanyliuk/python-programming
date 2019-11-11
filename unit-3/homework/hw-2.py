def encode_string(string):
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_list = ""
    for idx in string:
        for number in range(len(alphabet_list)):
            if idx == alphabet_list[number]:
        #when the letters of the string are equal to the alphabet list index position - they should be added to new list
                new_list += str((number + 1))
                
    
    return new_list

print(encode_string("emma"))