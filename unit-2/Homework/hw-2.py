# FT make $50 per hour up to 40 hours and then make $60 per hour
# PT make $65 per hour up to 20 hours and then $70 per hour
# Contract make $120 per hour but pay 25% tax

hours_worked = 30
worker_type = "full_time"


if hours_worked <= 40 and worker_type == "full_time":
    print (50 * hours_worked)
elif hours_worked > 40 and worker_type == "full_time": 
    print (50 * 40 + (hours_worked - 40) * 60)
   

if hours_worked <= 20 and worker_type == "part_time":
    print (65 * hours_worked)
elif hours_worked > 20 and worker_type == "part_time": 
    print (65 * 20 + (hours_worked - 20) * 70)


if worker_type == "contract":
    print (120 * hours_worked * .75)


  