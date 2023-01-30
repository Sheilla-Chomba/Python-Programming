# Below is the programming exercise
# (Financials: currency exchange) Write a program that prompts the user to enter
# the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
# Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
# vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to
# convert it to Chinese RMB or U.S. dollars, respectively

# Prompts user to type in the exchange rate and the manner in which they would like their money to be exchanged in
exchangeRate=eval(input("Enter the exchange rate from dollars to RMB: "))
choice=eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

while choice!=0 and choice!=1:
    choice = eval(input("Wrong input. Enter 0 to convert dollars to RMB and 1 vice versa: "))

if choice==0:
    dollar=eval(input("Enter the dollar amount: "))
    rmb=dollar*exchangeRate
    print(f"${dollar} is {rmb} yuan")
else:
    rmb = eval(input("Enter the RMB amount: "))
    dollar = rmb / exchangeRate
    print(f"{rmb} yuan is $",format(dollar,".2f"))