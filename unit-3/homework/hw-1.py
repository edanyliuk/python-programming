def emma_string(string):
    result = ""
    for character in string:
        result = character + result

    return result

print(emma_string("EmmaEmma"))

def palindrome(string):
    result = ""
    answer = ""
    for character in string:
        result = character + result
        if string == result:
            answer = True
        else:
            answer = False

    return answer

print(palindrome("racecar"))