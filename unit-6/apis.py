#use the requests module
import requests
import json

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")

#never do print(response)

data = response.json()

#print(data)
#print(type(data))

#print(json.dumps(data, indent = 4))
# above pretty print the result

#the below gets you the keys
print(data.keys())

#look at keys on the team object. below fails so you know is it a list cause it tells you. Use type to find out
# print(data["teams"].keys())

print(type(data["teams"]))

#look at the first item in this list
print(data["teams"][0])

#pretty print this.
#print(json.dumps(data["teams"][0], indent=4))

#save to a file
with open("nhl.json", "w") as nhl_file:
    nhl_file.write(json.dumps(data))

print("done...")
#once this is done you no longer have to connect to the api