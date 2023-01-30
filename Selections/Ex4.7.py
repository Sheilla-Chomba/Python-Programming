# Below is the programming exercise
# (Financial application: monetary units) Modify Listing 3.4, ComputeChange.py,
# to display the nonzero denominations only, using singular words for single units
# such as 1 dollar and 1 penny, and plural words for more than one unit such as 2
# dollars and 3 pennies.

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
    print(f"Your amount of {money} consists of:\n")
    if dollars == 1:
        print(f"\t {int(dollars)} dollar\n")
    else:
        print(f"\t {int(dollars)} dollars\n")
    if quarters == 1:
        print(f"\t {int(quarters)} quarter\n")
    else:
        print(f"\t {int(quarters)} quarters\n")
    if dimes == 1:
        print(f"\t {int(dimes)} dime\n")
    else:
        print(f"\t {int(dimes)} dimes\n")
    if nickels == 1:
        print(f"\t {int(nickels)} nickel\n")
    else:
        print(f"\t {int(nickels)} nickels\n")
    if pennies == 1:
        print(f"\t {int(pennies)} penny")
    else:
        print(f"\t {int(pennies)} pennies")

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

    print(f"Your amount of {money} consists of:\n")
    if dollars == 1:
        print(f"\t {int(dollars)} dollar\n")
    else:
        print(f"\t {int(dollars)} dollars\n")
    if quarters == 1:
        print(f"\t {int(quarters)} quarter\n")
    else:
        print(f"\t {int(quarters)} quarters\n")
    if dimes == 1:
        print(f"\t {int(dimes)} dime\n")
    else:
        print(f"\t {int(dimes)} dimes\n")
    if nickels == 1:
        print(f"\t {int(nickels)} nickel\n")
    else:
        print(f"\t {int(nickels)} nickels\n")
    if pennies == 1:
        print(f"\t {int(pennies)} penny")
    else:
        print(f"\t {int(pennies)} pennies")