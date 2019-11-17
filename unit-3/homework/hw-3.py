def pivot_split(integer_list, pivot):
    new_integer_list = []
    smaller_list = []
    bigger_list = []
    for number in integer_list:
        if number < pivot:
            smaller_list.append(number)
        else:
            bigger_list.append(number)
    
    new_integer_list.append(smaller_list)
    new_integer_list.append(bigger_list)
    
    return new_integer_list

print(pivot_split([1, 2, 3, 15, 1, 7], 3))

#could also do return[smaller_list, bigger_list] instead of my method