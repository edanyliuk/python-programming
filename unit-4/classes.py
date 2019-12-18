import json

#create a class. use keyword class to create a class. Capital letter is the name of a class.
class Person:
    #every class must have an init method. init is a special kind of function that is defined inside a class.
    #self is always at the start if you are talking about the data that belongs to the class.
    def __init__(self, name, age):
        #print('person object initialized')
        self.name = name
        self.age = age
        #name and age are parameters. the parameters can be anything..ie could be (self, n, a)
    
    def say_hello(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")




#how to instantiate a class. ie how to actually use it (create an object)
#uppercase are needed so you don't confuse it for a function.
#p is the object. whenever you initiate a class the init method is called.
p = Person("John", 35)

q = Person("Jane", 28)
print(p.name)

print(q.name)

#use a class method
p.say_hello()
q.say_hello()

print(type(p))
#we defined Person...normally the type is something that Python defined. We create our own data types

#create a rectangle class
#it should have a length and a width 
#it should have two method, perimeter and area

class Rectangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h 

    def area(self):
        #if you don't have self in the brackets then the method cannot access the class data
        aanswer = (self.base * self.height)
        return aanswer
    
    def perimeter(self):
        return (self.base + self.height) * 2
        

    

e = Rectangle(3, 4)

print(e.area())
print(e.perimeter())
print(f"Area is {e.area()} and perimeter is {e.perimeter()}")

#create a playlist class
#the playlist has a name and a list of tracks
#each track is a dictionary with title, artist, length of track

#write methods to add a track, to remove a track, to shuffle the playlist

track_file_name = "tracks.txt"

class Playlist:
    #list at the start is empty so you don't need a parameter for it
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add_track(self, title, artist, length):
        track = {}
        track["title"] = title
        track["artist"] = artist
        track["length"] = length
        self.tracks.append(track)

    def remove_track(self, title):
        for idx in range(len(self.tracks)):
            if title == self.tracks[idx]["title"]:
                break
        self.tracks.pop(idx)

    def save_tracks(self):
        #open file for writing. could use "tracks.txt" instead of making it a variable
        #takes files and puts them right into text ie dictionaries are one after another
        #dumps = dictionary to string and loads = string to dictionary
        with open(track_file_name, "w") as track_file:
            track_file.write(json.dumps(self.tracks))

#my attempt but legit no idea what i am doing.
    def load_tracks(self):
        #load the data from the tracks.txt file
        
        with open("tracks.json", "r") as music_file:
            music = json.load(music_file)
        
        #set the tracks variable to the data loaded in 

        self.tracks = music
        

new_playlist = Playlist("new music")

new_playlist.load_tracks()

print(new_playlist.tracks)

pl = Playlist("tunes")
pl.add_track("Shape of You", "Ed Sheeran", 3.45)
pl.add_track("Mamacita", "Tyga, Santata, YG", 4.15)

print(pl.tracks)

pl.remove_track("Shape of You")

print(pl.tracks)


pl.save_tracks()
