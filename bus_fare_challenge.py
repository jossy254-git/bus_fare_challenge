from datetime import datetime

#get current date 
date = datetime.date(datetime.now())
print("Date:", date)
#using today's date to get the day of the week
day = date.strftime("%A")
abbv = date.strftime('%a')
print("Day:", abbv)
# if statements
if day == "Sunday":
    print("Fare: 80")
elif day == "Saturday":
    print("Fare: 60")
else:
    print("fare: 100")