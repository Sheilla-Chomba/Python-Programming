# Below is the programming exercise
# (Financial application: payroll) Write a program that reads the following information
# and prints a payroll statement

# Prompts user to type in their payroll details
name=input("Enter Employee names: ")
hours=eval(input("Enter number of hours worked in a week: "))
while hours<0 or hours>168:
    hours = eval(input("Please indicate the right number of hours you worked. Enter number of hours worked in a week: "))
hourlyRate=eval(input("Enter hourly pay rate: "))
federalTax=eval(input("Enter Federal tax withholding rate: "))  # user needs to type in percentage
stateTax=eval(input("Enter State tax withholding rate: "))      # user needs to type in percentage

grossPay=hours*hourlyRate
federalTotal=(federalTax/100)*grossPay
stateTotal=(stateTax/100)*grossPay
deductions=stateTotal+federalTotal
netPay=grossPay-deductions

print(f"Employee name: {name}")
print(f"Hours worked: {hours}")
print(f"Pay rate: {hourlyRate}")
print("Gross Pay: $",format(grossPay,".2f"))
print("Deductions:")
print("\tFederal Withholding Tax (",federalTax,"%): ")
print("\tState Withholding Tax (",stateTax,"%): ")
print("\tTotal deductions: $",deductions)
print("Net Pay: $",format(netPay,".2f"))