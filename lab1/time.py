# time.py
# Yachitra Sivakumar, 121373093

mins_spent = int(input("How many minutes do you spend watching tv? "))

hours = int(mins_spent / 60)
minutes = int(mins_spent - (hours * 60))

print("There were", hours, "hours and", minutes, "minutes watching TV")
