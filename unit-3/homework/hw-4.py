def is_isogram(string):
    already_seen = []
    for character in string:
        if character in already_seen:
            return False
        else:
            already_seen.append(character)
    
    return True

#you can have multiple returns if you have multiple if then elses

print(is_isogram("python"))