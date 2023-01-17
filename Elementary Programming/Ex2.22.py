# Below is the programming exercise
# (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
# number of years and displays the population after that many years.

# Prompts user to type in the number of years
years=eval(input("Enter the number of years: "))

currentPop=312032486                            # Current Population
births=(years*365*24*3600)//7                   # Births
deaths=(years*365*24*3600)//13                  # Deaths
immigrants=(years*365*24*3600)//45              # Immigrants

futurePop=(currentPop+births+immigrants)-deaths     # The formula
print(f"The population after {years} will be: {futurePop}")