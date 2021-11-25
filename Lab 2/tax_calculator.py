#Lab 2 extra task - Tax Calculator
#our tax brackets are as follows
#£0-11000 = 0%
#£11,000-32,000 = 20%  
#£32,000-150,000 = 40%
#>£150,000 =45%
income = int(input("What is your income? "))
taxDue = 0
tax11k = 0
tax32k = 4200
tax150k = 47200
if income > 150000:
    taxDue = tax11k+tax32k+tax150k+((income-150000)*0.45)
elif income > 32000:
    taxDue = tax11k+tax32k+((income-32000)*0.4)
elif income > 11000:
    taxDue = tax11k+((income-11000)*0.2)
else:
    taxDue = 0
print("You are due to pay £" + str(taxDue) + " in taxes")