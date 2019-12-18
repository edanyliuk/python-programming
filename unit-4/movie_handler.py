import json

movie_file_name = "movies.txt"

class Movie:
    
    
    def __init__(self, title, genre, running_time):
        self.title = title
        self.genre = genre
        self.running_time = running_time
        self.casting = []
    #answer to number 2
    def add_cast(self, name):
        self.casting.append(name)

    def movie(self):
        #open file for writing. could use "tracks.txt" instead of making it a variable
        #takes files and puts them right into text ie dictionaries are one after another
        #dumps = dictionary to string and loads = string to dictionary
        with open(movie_file_name, "w") as movie_file:
            movie_file.write(json.dumps(self.casting))

    def describe_movie(self):
        print(self.title, self.genre, self.running_time, self.casting)
    
    def compare_to(self, other_movie):
        actor_counter = 0
        answer = 0
        for actor in self.casting:
            #print(actor)
            if actor in other_movie.casting:
                #print("if")
                actor_counter += 1
            if actor_counter >= 2:
                answer = 1
            else:
                answer = -1
        
        return answer

        
        


ml = Movie("Romy and Michele's High School Reunion", "Comedy", 92)
ml.add_cast("Mira Sorvino")
ml.add_cast("Lisa Kudrow")

pl = Movie("Madeup Movie", "Thriller", 123)
pl.add_cast("Mira Sorvino")
pl.add_cast("John Krasinski")


print(pl.casting)
print(ml.casting)

print(ml.compare_to(pl))



       