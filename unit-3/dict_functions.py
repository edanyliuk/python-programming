def frequency_counter(string):
    counter_output = {}
    if len(string) == len(set(string)):
        for letter in string:
            counter_output[letter] = 1
    else:
        for letter in string:
            counter_output[letter] = 0
        for letter in string:
            counter_output[letter] += 1

    return counter_output

print(frequency_counter("colette"))

#princeton's solution

def frequency_counterp(stringp):
    result = {}
    for character in stringp:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    
    return result

print(frequency_counterp("emma"))

def list_to_dict(string_list):
    dict_list = {}
    for new in string_list:
        dict_list[new[0]] = new[1]

    return dict_list

print(list_to_dict([['name','Alice'], ['job','Engineer'],['city','Toronto']]))
    
        
        

