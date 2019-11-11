#strings  are immutable. We cannot change a string
#strings are iterable

movie_title = "Thor, the Dark World"

#print(movie_title[0])

#movie_title[5] = " - " #this is not allowed
#Once the string has been declared you cannot change it. You can re-assign movie_title

movie_title = "The Avengers"
#this is reassignment

start = movie_title[0:2]
#starts from position 0 and grabs up to position 2 but excludes position 2 (which would be the third character)

#Indices can also be negative. -1 gives you the last character

#If you are starting with position 0 then you can just do [:x number] and if you do [x number:] then it goes to the end
#you can use [:x number] with x number being negative.
print(movie_title[-1])

print(start)

print(movie_title[:4])

print(movie_title[2:])