destinations = ["Cozumel", "Cancun", "Montego Bay", "Bora Bora", "Maui", "Phuket", "Mykonos", "Palawan", "Vieques", "Negril"]
countries = ["Mexico", "Mexico", "Jamaica", "Tahiti", "USA", "Thailand", "Greece", "Philippines", "Puerto Rico", "Jamaica"]
#countries must be in order of destination

for idx in range(len(destinations)):
    destinations[idx] += " - " + countries[idx]

print(destinations)

print(len(destinations))