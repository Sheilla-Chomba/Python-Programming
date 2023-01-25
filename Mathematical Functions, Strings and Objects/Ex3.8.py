# Below is the programming exercise
# (Financial application: monetary units) Rewrite Listing 3.4, ComputeChange.py,
# to fix the possible loss of accuracy when converting a float value to an int value.
# Enter the input as an integer whose last two digits represent the cents. For example,
# the input 1156 represents 11 dollars and 56 cents.

# Prompts user to type in the money they have
money=eval(input("Enter the amount of money you have: "))

if (money*100)%100==0:        # Incase user inputs an integer as money
    cents = money           # indicates that the money has been typed in cents form
    dollars = cents // 100  # Extracts dollars from the money
    remCents = cents % 100  # Extracts the remaining cents after removing dollars
    quarters = remCents // 25  # Extracts quarters from the money
    remCents2 = remCents % 25  # Extracts the remaining cents after removing quarters
    dimes = remCents2 // 10  # Extracts dimes from the money
    remCents3 = remCents2 % 10  # Extracts the remaining cents after removing dimes
    nickels = remCents3 // 5  # Extracts  nickels from the money
    pennies = remCents3 % 5  # Extracts pennies from the money since thats the only amount left
    print(f"Your amount of: {money} consists of:\n"
          f"\t {int(dollars)} dollars\n"
          f"\t {int(quarters)} quarters\n"
          f"\t {int(dimes)} dimes\n"
          f"\t {int(nickels)} nickels\n"
          f"\t {int(pennies)} pennies")
else:
    cents = money * 100  # converts the money to cents
    dollars = cents // 100  # Extracts dollars from the money
    remCents = cents % 100  # Extracts the remaining cents after removing dollars
    quarters = remCents // 25  # Extracts quarters from the money
    remCents2 = remCents % 25  # Extracts the remaining cents after removing quarters
    dimes = remCents2 // 10  # Extracts dimes from the money
    remCents3 = remCents2 % 10  # Extracts the remaining cents after removing dimes
    nickels = remCents3 // 5  # Extracts  nickels from the money
    pennies = remCents3 % 5  # Extracts pennies from the money since thats the only amount left

    print(f"Your amount of: {money} consists of:\n"
          f"\t {int(dollars)} dollars\n"
          f"\t {int(quarters)} quarters\n"
          f"\t {int(dimes)} dimes\n"
          f"\t {int(nickels)} nickels\n"
          f"\t {int(pennies)} pennies")

