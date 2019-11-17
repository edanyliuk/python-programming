#sets do not allow duplicates

rainbow_colors = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}

print(type(rainbow_colors))
#tells you that this is a set. sets are lists with no duplicates. uses same notation as dictionaries 
#sets are not ordered -> ie no notion of 0 index and looking at positions

values = [1, 5, 7, 3, 5, 5, 9, 7]
#set function takes a list and makes it into a set
unique_values = set(values)
print(unique_values)

#for sets, use .add instead of .append
unique_values.add(105)

print(unique_values)

#to remove a value from a set use remove
unique_values.remove(3)

print(unique_values)
#if you try to remove something that isn't htere it will give you a KeyError: (insert value that you tried to remove that wasn't there)

#we can create sets from iterable ie we can create sets from strings

#single line is_isogram
def is_isogram(string):
    return len(string) == len(set(string))
        
print(is_isogram("hi"))

#tuples are immutable ie cannot be changed. you can access values via indices. Tuples are ordered. We can have duplicates but we cannot change them.
#tuples work like a list but cannot be changed. use () as opposed to []
weekdays = ("Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun")

# weekdays[6] = "Dom"
#will give an error

#you can however index it.
print(weekdays[0])
