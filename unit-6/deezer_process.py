import json

with open("deezercardi.json", "r") as cardi_file:
    cardi = json.load(cardi_file)

with open("deezered.json", "r") as ed_file:
    edsheeran = json.load(ed_file)

with open("deezereminem.json", "r") as eminem_file:
    eminem = json.load(eminem_file)

#print(type(eminem))

#print(eminem.keys())

#print(eminem["data"][0])

#3. For each artist
#a) How many tracks are listed 

cardi_tracks = []
cardi_count = 0

for track in cardi["data"]:
    cardi_tracks.append(track["title"])
cardi_count = len(cardi_tracks)

print(cardi_count)

eminem_tracks = []
eminem_count = 0

for slimshady in eminem["data"]:
    eminem_tracks.append(slimshady["title"])
eminem_count = len(eminem_tracks)

print(eminem_count)

edsheeran_tracks = []
edsheeran_count = 0

for edtracks in edsheeran["data"]:
    edsheeran_tracks.append(edtracks["title"])
edsheeran_count = len(edsheeran_tracks)

#print(edsheeran_tracks)
print(edsheeran_count)

#b) how many albums are listed

cardi_albums = []
cardi_count = 0
for albums in cardi["data"]:
    cardi_albums.append(albums["album"]["title"])

cardi_count = len(set(cardi_albums))
print(cardi_count)

eminem_albums = []
eminem_count = 0
for slim_albums in eminem["data"]:
    eminem_albums.append(slim_albums["album"]["title"])

eminem_count = len(set(eminem_albums))

#print(eminem_albums)
print(eminem_count)

ed_albums = []
ed_count = 0
for eddy in edsheeran["data"]:
    ed_albums.append(eddy["album"]["title"])

ed_count = len(set(ed_albums))
#print(ed_albums)
print(ed_count)

cardi_explicit_count = 0
cardi_explicit_songs = []
for cardi_ex in cardi["data"]:
    if cardi_ex["explicit_lyrics"] == True:
        cardi_explicit_count += 1
        cardi_explicit_songs.append(cardi_ex["title"])

print(cardi_explicit_count)
#print(len(cardi_explicit_songs))
#print(cardi_tracks)

eminem_explicit_count = 0
eminem_explicit_songs = []
for slim_ex in eminem["data"]:
    if slim_ex["explicit_lyrics"] == True:
        eminem_explicit_count += 1
        eminem_explicit_songs.append(slim_ex["title"])

print(eminem_explicit_count)
#print(len(eminem_explicit_songs))

ed_explicit_count = 0
ed_explicit_songs = []

for ed_ex in edsheeran["data"]:
    if ed_ex["explicit_lyrics"] == True:
        ed_explicit_count += 1
        ed_explicit_songs.append(ed_ex["title"])

print(ed_explicit_count)

#d) which year was the most recent album for each?

#SKIP

#4 When was the release date for Eminem's album titled "The Eminem Show"?

#SKIP

#6. How many tracks were on Ed Sheeran's album "Shape of You"

shape_count = 0
shape_songs = []

for shapeofyou in edsheeran["data"]:
    if shapeofyou["album"]["title"] == "Shape of You":
        shape_count += 1
        shape_songs.append(shapeofyou["title"])

print(shape_count)
print(ed_albums)


#7. Which artists collaborated iwth Cardi B on Cardi B?
collaborators = []
collab_count = 0
for collab in cardi["data"]:
    if collab["title"] == "Cardi B":
        collaborators.append(collab["artist"]["name"])
        collab_count += 1

print(collab_count)
print(collaborators)

