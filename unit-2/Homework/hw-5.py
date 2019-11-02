temperature_readings = [25, 18, -5, 11, -15, 8, -18, 6, 13]
positive_readings = 0
negative_readings = 0
negative_count = 0
positive_count = 0

for temp in temperature_readings:
    if temp > 0:
        positive_readings += temp
        positive_count += 1
    elif temp < 0:
        negative_readings += temp
        negative_count += 1



print(f"Average of positive readings is {positive_readings / positive_count}")
print(f"Average of negative readings is {negative_readings / negative_count}")
