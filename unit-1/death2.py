
def victims(people):
    victim_total = 0
    for idx in range(len(people)):
        if people[idx].isnumeric() and people[idx + 1] == " " and people[idx - 1].isnumeric() == False:
            victim_total += int(people[idx])
        elif people[idx].isnumeric() and people[idx + 1].isnumeric() and people[idx + 2] == " " and people[idx - 1].isnumeric() == False:
            victim_total += int(people[idx] + people[idx+1])
        elif people[idx].isnumeric() and people[idx + 1].isnumeric() and people[idx + 2].isnumeric() and people[idx + 3] == " " and people[idx - 1].isnumeric() == False:
            victim_total += int(people[idx] + people[idx+1] + people[idx+2])
        else:
            victim_total += 0
    
    return victim_total

print(victims("12 White Male(s)"))

#10 White Female(s)6 White Male(s)
#"129 White 2 Native American 5 Latino 32 Black"