movie_titles = ["The Incredible Hulk", "The Avengers", "Iron Man", "Thor", "Guardians of the Galaxy", "Ant Man", "Black Panther", "Iron Man 2", "Iron Man 3", "Captain America"]
special_marvel_movies = []

for movie in movie_titles:
    if "the " in movie or "The " in movie:
        special_marvel_movies.append(movie)

print (special_marvel_movies)