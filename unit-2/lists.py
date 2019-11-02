'''

cohort_4 = ["Emma", "Allaina", "Chizea", "Clark", "Daniela", "Julian", "Kyle", "Christina", "Lizhi", "Keerthi", "Sahil", "Shilaj", "Princeton"]

print(len(cohort_4))

#access items in list using position (index)

print(cohort_4[0]) #prints first item in list

print(cohort_4)

#add items to the list, use append
cohort_4.append("Catherine")

print(type(cohort_4))

print(cohort_4)

#remove an item from the list, use remove
cohort_4.remove("Emma")

print(cohort_4)



#this is wrong below. need to use the type function
values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40.0, 85.6, 77.1]
float_values = []

for floats in values:
    if floats % 2 != 0 and floats % 2 != 1:
        float_values.append(floats)

print(float_values)


#create a new list with only the floats
values = [2.3, 45, 11, -5, 3.5, 7.9, 11.7, 40.0, 85.6, 77.1]
float_values = []

for value in values:
    if type(value) is float:
        float_values.append(value)

print(float_values)

'''

#find averages of these three lists and store them in a new list
weights = [[50, 25, 75], [95.7, 38.3, 55.2], [88, 45, 16]]
averages = []


for item in weights:
    list_total = 0
    for value in item:
        list_total += value
    averages.append(list_total/len(item))

print(averages)

'''
#print
*
**
***
****
*****
******
*******
********
*********
**********

for row in range(1, 11):
    for col in range(1, row + 1):
        print("*", end = "")
    print()


#a different solution without a look within a loop
for i in range(0, 11):
    print("*" * (i + 1))

'''

#using indexes to assess list items
#use index if we need to edit items in list

#set all negative readings to 0
readings = [3.5, -7.7, -9.8, 13.6, 22.5, 19.7, -8.6]

for idx in range(len(readings)):
    if readings[idx] < 0:
        readings[idx] = 0

print(readings)

#find the position of an item in a list

current_age = 25
ages = [15, 17, 27, 35, 12, 25, 55, 40, 31, 20]

for idx in range(len(ages)):
    if current_age == ages[idx]:
        print(f"current_age is in position {idx}")