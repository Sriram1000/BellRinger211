#Take the time in your own time zone and output how long in minutes till the class ends.

minutes_started = int(input("How many minutes has it been since class started? Enter an integer: "))

minutes_left = 59 - minutes_started

minutes_left = str(minutes_left)

print ("There are", minutes_left,"minutes left in class!")
