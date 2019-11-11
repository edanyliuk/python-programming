#this is identical to how you did it

temperature_readings = [25, 18, -5, 11, -15, 8, -18, 6, 13]
positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

for reading in temperature_readings:
    if reading > 0:
        positive_sum += reading
        positive_count += 1
    else: 
        negative_sum += reading
        negative_count += 1

print(f"Average of positive readings is {positive_sum / positive_count}")
print(f"Average of negative readings is {negative_sum / negative_count}")

# you did it a bit different 

movie_titles = ["The Incredible Hulk", "The Avengers", "Iron Man", "Thor", "Guardians of the Galaxy", "Ant Man", "Black Panther", "Iron Man 2", "Iron Man 3", "Captain America"]
special_marvel_movies = []

for movie in movie_titles:
    if "the " in movie.lower():
        special_marvel_movies.append(movie)

print (special_marvel_movies)
