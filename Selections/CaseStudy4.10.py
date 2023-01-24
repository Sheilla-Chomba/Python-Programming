# Below is a case study to compute taxes

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
   if income>=0 and income<8350:
       taxRate=10
   elif income > 8350 and income < 33950:
       taxRate = 15
   elif income >33950 and income < 82250:
       taxRate = 25
   elif income > 82250 and income < 171550:
       taxRate = 28
   elif income > 171550 and income < 372950:
       taxRate = 33
   else:
       taxRate =35
   netPay=income-((income*taxRate)/100)
   print("The net income is $",format(netPay,".2f"))
elif status==2:
    if income >= 0 and income < 16700:
        taxRate = 10
    elif income > 16700 and income < 67900:
        taxRate = 15
    elif income > 67900 and income < 131050:
        taxRate = 25
    elif income > 131050 and income < 208850:
        taxRate = 28
    elif income > 208850 and income < 372950:
        taxRate = 33
    else:
        taxRate = 35
    netPay = income - ((income * taxRate) / 100)
    print("The net income is $",format(netPay,".2f"))
elif status==3:
    if income >= 0 and income < 8350:
        taxRate = 10
    elif income > 8350 and income < 33950:
        taxRate = 15
    elif income > 33950 and income < 68525:
        taxRate = 25
    elif income > 68525 and income < 104425:
        taxRate = 28
    elif income > 104425 and income < 186475:
        taxRate = 33
    else:
        taxRate = 35
    netPay = income - ((income * taxRate) / 100)
    print("The net income is $",format(netPay,".2f"))
else:
    if income >= 0 and income < 11950:
        taxRate = 10
    elif income > 8350 and income < 45500:
        taxRate = 15
    elif income > 45500 and income < 117450:
        taxRate = 25
    elif income > 117450 and income < 190200:
        taxRate = 28
    elif income > 190200 and income < 372950:
        taxRate = 33
    else:
        taxRate = 35
    netPay = income - ((income * taxRate) / 100)
    print("The net income is $",format(netPay,".2f"))