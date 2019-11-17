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

def list_to_dict(string_list):
    dict_list = {}
    for new in string_list:
        dict_list[new[0]] = new[1]

    return dict_list

print(list_to_dict([['name','Alice'], ['job','Engineer'],['city','Toronto']]))
    
        
        

