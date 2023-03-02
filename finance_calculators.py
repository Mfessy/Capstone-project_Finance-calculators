import math

#ask the user to choose aither bond or investment
user_choice = input("Choose either 'bond' or 'investment' from the list below: ")

if user_choice == "investment":
    print("to calculate the amount of interest you'll earn on your investment: ")
    amount = float(input("Enter the amount of money to invest "))
    interest_rate = float(input("Enter interest rate "))
    years = int(input("number of years to invest "))
    interest = input("simple or compound ")
# investment calculations 
    r = interest_rate/100
    P = amount
    t = years

    if interest == "simple":
        A = P*(1+r*t)
        print(A)
    else:
        interest == "compound"
        A = P* math.pow((1+r),t)
        print("The return on investment will be " + str(A))

if  user_choice == "bond":
    print("to calculate the amount of money you'll pay on your home loan: ")
    value = float(input("Enter present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    duration = int(input("Enter number of months to repay the loan: "))
    
    # bond calculations
    
    P = value
    i = interest_rate/12
    n = duration
    x = (i*P)/(1-(1+i)*(-n))
    print("The amount you are going to pay on your bond is: " + str(x))

if user_choice != "investment" and user_choice != "bond":
    print("invalid choice, please check and enter again ")
    

    



               
