# Below is the programming exercise
# (Find the number of years and days) Write a program that prompts the user to
# enter the minutes (e.g., 1 billion), and displays the number of years and days for
# the minutes. For simplicity, assume a year has 365 days.

# Prompts user to type in the time in minutes
minutes=eval(input("Enter the time in minutes: "))

days=minutes//(24*60)       # Converts minutes to days without putting any decimal
years=days//365             # Converts days to years without putting any decimal
actualDays=int(days%365)    # Returns the days remaining after subtracting all years

print(f"{minutes} minutes is {years} years and {actualDays} days")  # prints out the results