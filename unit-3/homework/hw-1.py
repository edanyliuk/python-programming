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

#Princeton's solution

def reverse_list(my_list):
    result = []
    idx = len(my_list) - 1
    while idx >= 0:
        result.append(my_list[idx])
        idx -= 1
    
    return result

print(reverse_list([1, 4, 5, 6]))
