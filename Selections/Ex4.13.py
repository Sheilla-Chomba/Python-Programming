# Below is the programming exercise
# (Financial application: compute taxes) Listing 4.7, ComputeTax.py, gives the
# source code to compute taxes for single filers. Complete Listing 4.7 to give the
# complete source code for the other filing statuses.

# Prompts user to type in their married status
status=eval(input(" \tEnter 1 for single"
                  "\n \tEnter 2 for married filing jointly"
                  "\n \tEnter 3 for married filing separately"
                  "\n \tEnter 4 for head of household"
                  "\n In what status are you filing your taxes in: "))
while status<=0 or status>4:
    status = eval(input("Wrong input. Kindly type in again."
                        "\n \tEnter 1 for single"
                        "\n \tEnter 2 for married filing jointly"
                        "\n \tEnter 3 for married filing separately"
                        "\n \tEnter 4 for head of household"
                        "\n In what status are you filing your taxes in: "))

income=eval(input("Enter the income you are earning: "))
while income<0:
    income = eval(input("Wrong input. Enter the income you are earning: "))

if status==1:
   if income>=0 and income<=8350:
       tax=(income*10)/100
   if income > 8350 and income <= 33950:
       tax=(income-8350)*(15/100)+(8350*(10/100))
   if income >33950 and income <= 82250:
       tax = (income - 33950) * (25 / 100)+(8350*(10/100))+((33950-8350)*(15/100))
   if income > 82250 and income <= 171550:
       tax = (income - 82250) * (28 / 100)+(8350*(10/100))+((33950-8350)*(15/100))+((82250-33950)*(25/100))
   if income > 171550 and income <= 372950:
       tax = (income - 171550) * (33 / 100)+(8350*(10/100))+((33950-8350)*(15/100))+((82250-33950)*(25/100))+((171550-82250)*(28/100))
   if income>372950:
       tax = (income - 372950) * (35 / 100)+(8350*(10/100))+((33950-8350)*(15/100))+((82250-33950)*(25/100))+((171550-82250)*(28/100))+((372950-171550)*(33/100))
   print("The tax is $",format(tax,".2f"))
elif status==2:
    if income >= 0 and income <= 16700:
        tax = (income * 10) / 100
    if income > 16700 and income <= 67900:
        tax=(income-16700)*(15/100)+(16700*(10/100))
    if income > 67900 and income <= 131050:
        tax = (income - 67900) * (25 / 100)+(16700*(10/100))+((67900-16700)*(15/100))
    if income > 131050 and income <= 208850:
        tax = (income - 82250) * (28 / 100)+(16700*(10/100))+((67900-16700)*(15/100))+((131050-67900)*(25/100))
    if income > 208850 and income <= 372950:
        tax = (income - 171550) * (33 / 100)+(16700*(10/100))+((67900-16700)*(15/100))+((131050-67900)*(25/100))+((208850-131050)*(28/100))
    if income>372950:
        tax = (income - 171550) * (35 / 100)+(16700*(10/100))+((67900-16700)*(15/100))+((131050-67900)*(25/100))+((208850-131050)*(28/100))+((372950-208850)*(33/100))
    print("The tax is $", format(tax, ".2f"))
elif status==3:
    if income >= 0 and income < 8350:
        tax = (income * 10) / 100
    if income > 8350 and income < 33950:
        tax=(income-8350)*(15/100)+(8350*(10/100))
    if income > 33950 and income < 68525:
        tax = (income - 33950) * (25 / 100)+(8350*(10/100))+((33950-8350)*(15/100))
    if income > 68525 and income < 104425:
        tax = (income - 68525) * (28 / 100)+(8350*(10/100))+((33950-8350)*(15/100))+((68525-8350)*(25/100))
    if income > 104425 and income < 186475:
        tax = (income - 104425) * (33 / 100)+(8350*(10/100))+((33950-8350)*(15/100))+((68525-8350)*(25/100))+((104425-68525)*(28/100))
    if income>186475:
        tax = (income - 186475) * (35 / 100)+(8350*(10/100))+((33950-8350)*(15/100))+((68525-8350)*(25/100))+((104425-68525)*(28/100))+((186475-104425)*(33/100))
    print("The tax is $", format(tax, ".2f"))
else:
    if income >= 0 and income < 11950:
        tax = (income * 10) / 100
    if income > 11950 and income < 45500:
        tax=(income-11950)*(15/100)+(11950*(10/100))
    if income > 45500 and income < 117450:
        tax=(income-45500)*(25/100)+(11950*(10/100))+((45500-11950)*(15/100))
    if income > 117450 and income < 190200:
        tax=(income-117450)*(28/100)+(11950*(10/100))+((45500-11950)*(15/100))+((117450-45500)*(25/100))
    if income > 190200 and income < 372950:
        tax=(income-190200)*(33/100)+(11950*(10/100))+((45500-11950)*(15/100))+((117450-45500)*(25/100))+((190200-117450)*(28/100))
    if income>372950:
        tax=(income-372950)*(35/100)+(11950*(10/100))+((45500-11950)*(15/100))+((117450-45500)*(25/100))+((190200-117450)*(28/100))+((372950-190200)*(33/100))
    print("The tax is $", format(tax, ".2f"))