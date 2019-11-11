def emma_string(string):
    result = ""
    for character in string:
        result = character + result

    return result

print(emma_string("EmmaEmma"))