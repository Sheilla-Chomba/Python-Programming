# Below is a case study to show the amount of money in dollars, quarters, dimes, nickels and pennies

# Prompts user to type in the amount of money
money=eval(input("Enter the amount of money you have: "))

cents=money*100         # converts the money to cents
dollars=cents//100      # Extracts dollars from the money
remCents=cents%100      # Extracts the remaining cents after removing dollars
quarters=remCents//25   # Extracts quarters from the money
remCents2=remCents%25   # Extracts the remaining cents after removing quarters
dimes=remCents2//10     # Extracts dimes from the money
remCents3=remCents2%10  # Extracts the remaining cents after removing dimes
nickels=remCents3//5    # Extracts  nickels from the money
pennies=remCents3%5     # Extracts pennies from the money since thats the only amount left

print(f"Your amount of: {money} consists of:"
      f"\t {int(dollars)} dollars\n"
      f"\t {int(quarters)} quarters\n"
      f"\t {int(dimes)} dimes\n"
      f"\t {int(nickels)} nickels\n"
      f"\t {int(pennies)} pennies")