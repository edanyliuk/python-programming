import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"ed sheeran"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "ea4236e72amshf300c19184d66d2p19e50fjsn52eafbaa8576"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

#print(data)
print(type(data))

#print(json.dumps(data, indent = 4))
# above pretty print the result

#the below gets you the keys
#print(data.keys())

#look at keys on the team object. below fails so you know is it a list cause it tells you. Use type to find out
# print(data["teams"].keys())

#print(type(data["data"]))


#look at the first item in this list
#print(data["data"][0])

with open("deezered.json", "w") as ed_file:
    ed_file.write(json.dumps(data))

