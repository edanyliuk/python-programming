def add(num1, num2):
    return num1 + num2
#you write a function to do something. Something it will return something and sometimes it doesn't. 
#Use return for a function that calculates something - it gives you the answer
#this function adds two integers
print(add(5, 10)) #pass to print function

result = add(50, 20) #assign to a variable. always name your variables to reflect what they're doing ie num1 and num2

#parameter vs argument. important to understand when we use which
#function may or may not have parameters. Can be 0
#we use a function by calling it. ie print() the thing inside () are the arguments
#num1 and num2 are parameters

#function has no parameters and takes no arguments when were calling it.
#when were calling it we give it arguments
#this function displays hello there
def say_hello():
    print("Hello there!")

say_hello()

#cannot use your function before it is defined





#function that returns the length of a string
def length(string):
    return len(string)

print(length("hi there"))

#function to return the sum of integers in a list
#use is to compare types
def sum_of_integers(a_list):
    result = 0
    for num in a_list:
        if type(num) is int:
            result += num

    return result

print(sum_of_integers([1, 2, 3, "a"]))

#function to reverse a string. the while loop is used to count backwards
def rev_string(string):
    idx = len(string) - 1
    result = ""
    while idx >= 0:
        result += string[idx]
        idx -= 1

    return result

print(rev_string("Emma"))

#reverse string in one line (python)

def one_line_reverse(string):
    return string[::-1]

print(one_line_reverse("Emmasmalll"))

#using a for loop - Daniela's version. This puts the first part last. Will find the first letter in the string and then add to result which is blank. Then it keeps adding

def daniela_reverse(string):
    result = ""
    for character in string:
        result = character + result

    return result

print(daniela_reverse("HIIIIITINY"))