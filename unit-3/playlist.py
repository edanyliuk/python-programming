playlists = [{"title": "Dangerous Woman", "genre": "Pop", "artist": "Ariana Grande", "year": "2016", "length": 3.56}, 
{"title": "Into You", "genre": "Pop", "artist": "Ariana Grande", "year": "2016", "length": 4.04},
{"title": "Peanut Butter Jelly", "genre": "Dance", "artist": "Galantis", "year": "2015", "length": 3.24},
{"title": "Peanut Butter Jelly", "genre": "Dance", "artist": "Galantis", "year": "2015", "length": 3.48},
{"title": "Slide", "genre": "Dance", "artist": "Calvin Harris", "year": "2017", "length": 3.51},
{"title": "Heatstroke", "genre": "Dance", "artist": "Calvin Harris", "year": "2017", "length": 3.49},
{"title": "Something", "genre": "Rock", "artist": "The Beatles", "year": "1969", "length": 3.03},
{"title": "All for You", "genre": "Pop", "artist": "Janet Jackson", "year": "2001", "length": 5.28},
{"title": "Stronger", "genre": "Rap", "artist": "Kanye West", "year": "2007", "length": 5.11},
{"title": "Rehab", "genre": "R&B", "artist": "Amy Winehouse", "year": "2006", "length": 3.35}]

#answer to number 1
for playlist in playlists:
    print (playlist["title"])

#answer to number 2
artist_list =[]
for playlist in playlists:
    artist_list.append((playlist["artist"]))
print(set(artist_list))

#answer to number 3
total_length_secs = 0
total_length_mins = 0
total_length_hours = 0

length_list = []
for playlist in playlists:
    length_list.append((playlist["length"]))
for idx in range(len(length_list)):
    total_length_secs += (length_list[idx] - int(length_list[idx])) * 100 + (int(length_list[idx]) * 60)
    total_length_mins = total_length_secs / 60
    total_length_hours = total_length_mins / 60


print(total_length_secs)
print(total_length_mins)
print(total_length_hours)

