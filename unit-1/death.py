def victims(people):
    victim_total = 0
    victim_list = people.split()

    for letter in people:
        if letter.isnumeric():
            victim_total += int(letter)



    return(victim_total)