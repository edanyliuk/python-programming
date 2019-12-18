#list compregension can be used to create a new list from
# an exiting one

nums = [1, 3, 6, 8, 9, 11, 15, 18]

#create a new list with only the even numbers

even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

#with list comprehension this can be done with one line

new_even_nums = [num for num in nums if num % 2 == 0]

print(new_even_nums)

#take the even numbers and square them
#start is what you want the append to be
#start with for then do the if (condition) then put the append at the start but do this last
even_square = [val ** 2 for val in nums if val % 2 == 0]

print(even_square)

#create a list of the titles with "t" in their names

titles = ["Lord of the rings", "The time machine", "The Great Gatsby", "Moby Dick", "Chronicles of Narnia"]
t_titles = [title for title in titles if "t" in title]
print(t_titles)

#convert a string to uppercase using list comprehension

string = "emma is cool"
# "".join([xyz in list]) will make it a string
#join is the opposite of split
upper_case = "".join([letter.upper() for letter in string])

print(upper_case)

#if/else goes before the for
#if number is less than 10, add ten, else subtract ten
vals = [15, 12, 3, 8, -1, 7, 11, 25, 0, 10]
ten_list = [val + 10 if val < 10 else val - 10 for val in vals]


print(ten_list)

#dictionary comprehension
person = {"Name": "Alice", "Job": "Engineer", "City": "Toronto"}
#create a new dictionary that has the first intial of both key and value
new_dict = {key[0]:value[0] for key, value in person.items()}

print(new_dict)