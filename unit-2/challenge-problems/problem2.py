'''
num = 7
num_lists = [2, 5, 7, 8, 14]
multiple_num = []

for num_list in num_lists:
    multiple_num.append(num * num_list)

print (multiple_num)

friends = ["Emma", "John", "Peter"]
new_friends = []
for idx in range(len(friends)):
    if len(friends[idx]) == 4:
        new_friends.append(friends[idx])

print (new_friends)
'''


# .isdigit() verifies if a character in a string is a digit