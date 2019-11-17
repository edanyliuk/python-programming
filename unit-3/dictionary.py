#a {} is used for a dictionary. Inside you have key value pairs


#a dictionary is a collection of key/value pairs
#dictionary isn't ordered
#access not using position - but index(like an index in a book)

student = {"name": "Emma", "age": 25, "address": "Toronto"}

#access elements in a dictionary
print (student["name"])
print (student["age"])
print (student["address"])

#a dictionary cannot have duplicate keys
#keys must be unique

#add items to a dictionary
car = {} #this creates an empty dictionary

car["make"] = "Toyota"
car["model"] = "Prius"
car["year"] = 2019
car["color"] = "Silver"

print(car)
#uses by default an ordered dictionary ie it is in the order that you put the keys in. Assume that it is not in order

car["year"] = 1997

print(car)

#will override - it cannot have duplicate keys it will override it

for item in car:
    print(car[item])
#gives values
for item in car:
    print(item)
#gives keys

#using for & in loop will return the keys - not the values
#to get the values use dictionary title[item]

#make a list of dictionaries

cars = [{'make': 'Toyota', 'model': 'Prius', 'year': 1997, 'color': 'Silver'}, 
{'make': 'Lexus', 'model': 'Prius', 'year': 2007, 'color': 'Blue'}, 
{'make': 'Toyota', 'model': 'Camry', 'year': 2011, 'color': 'Green'}, 
{'make': 'Hyundai', 'model': 'Sonata', 'year': 2018, 'color': 'White'}]


print(cars)

for car in cars: #car will be a dictionary
    print(type(car))

total_toyota = 0
for car in cars:
    if car['make'] == 'Toyota':
        total_toyota += 1

print(total_toyota)

#to get a value always use a key except dictionaries or lists but a value can be anything including dictionaries or lists

#write a function called frequency_counter(string)
#return the frequency of each letter in the string

#frequency_counter("a testy line of text")
#will return:
#"a": 1
#" ": 4
#"t": 2
#"e": 2
# ...continue

#use a dictionary

#how to get the keys
#use the keys method
print(car.keys())

#how do we get the values
#use the values method
print(car.values())

#to get both keys and values
#the (key, value) is called a tuple
#use the items method
print(car.items())

#because there is a tuple, you have key, value
#prints the tuples line by line (2 at a time)
for key, value in car.items():
    print(key, value)