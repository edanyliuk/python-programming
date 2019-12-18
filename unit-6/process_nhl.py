import json

with open("nhl.json", "r") as nhl_file:
    data = json.load(nhl_file)

print(type(data))

#get keys
print(data.keys())

#print first item so you know the structure and what the types of values look like
# print(data["teams"][0])




#how many teams are in the NHL?
teams_list =[]
answer = 0
for team in data["teams"]:
    teams_list.append(team["name"])

answer = len(set(teams_list))

print(answer)







#when were the Boston Bruins started?

year = ""
for team in data["teams"]:
    if team["name"] == "Boston Bruins":
        year = team["firstYearOfPlay"]

print(year)






#what is the oldest team in the NHL?


oldest_team_years = []
for team in data["teams"]:
    oldest_team_years.append(team["firstYearOfPlay"])
   
string_conversion = []
for oldest in oldest_team_years:
    string_conversion.append(int(oldest))

# print(string_conversion)

oldest_answer = min(string_conversion)

# print(oldest_answer)
team_name = ""

for team in data["teams"]:
    if team["firstYearOfPlay"] == str(oldest_answer):
        team_name = team["name"]

print(team_name)

# print(oldest_team_years)
# print(oldest_team)





#What are the teams in the Eastern conference?

eastern_names = []
for team in data["teams"]:
    if team["conference"]["name"] == "Eastern":
        eastern_names.append(team["name"])

print(eastern_names)
