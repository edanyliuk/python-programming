import json

'''
#don't name your file json
person = {"Name": "Alice", "Job": "Engineer", "City": "Toronto"}

print(type(person))
'''

#properly formatted json
#keys enclosed in double quotations
#enclosed with curly braces, square brackets can be used
#no comments in json

with open("cohort_4.json", "r") as cohort_file:
    cohort = json.load(cohort_file) # converts json file to python dictionary/list

print(type(cohort))
print(json.dumps(cohort, indent = 2)) #present info better than print(cohort). Dumps takes a dictionary and makes it into a string
#2 and 4 are the most common indents