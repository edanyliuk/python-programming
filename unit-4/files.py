#how to read a file
'''
my_file = open("lines.txt", "r")
#r is for reading and a is for appending. when it is being read you have access to data
#can read files that aren't in directory (ie in this case from a unit other than 4) but you must use the file pathway
data = my_file.read()

my_file.close()

print(data)

#how do we write to a file
my_file = open("lines.txt", "w")
#w is for writing (ie it writes over it) and a is for append. If the file doesn't exist it will create one.
my_file.write("Please add this new line")
my_file.close()

my_file = open("new_file.txt", "w")
my_file.write("Lines for my new file")
my_file.close()

#to add to the end of a file use append (a). it will literally add it right to the end. need \n for a new line
my_file = open("new_file.txt", "a")
my_file.write("\nNew file should have new line as well")
my_file.close()
'''
#we can use "with" if we don't want to have to close every time
with open("lines.txt", "r") as text_file:
    data = text_file.read()

print(data)