# time.py
# Yachitra Sivakumar, 121373093


def spent(question_string):
    # gathers input from user and makes it an integer
    mins_spent = int(input(question_string))
    # converts minutes to hours
    hours = int(mins_spent / 60)
    # converts total hours into minutes and finds remainder of minutes
    minutes = int(mins_spent - (hours * 60))
    # returns time spent in hours and minutes
    return print("There were", hours, "hours and", minutes, "minutes watching TV")

# allows user to input minutes into the function
spent("how many minutes do you spend watching tv? ")
