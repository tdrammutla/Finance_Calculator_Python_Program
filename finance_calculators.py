import math

# This program allows the user to access two different financial calculators,an investment calculator and a home loan repayment calculator


print("\n")

print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")

# Options they can choose from

print("investment - to calculate the amount of interest you'll earn on interest")
print("bond - to calculate the amount you'll have to pay on home loan")
print("\n")

# Prompting user to choose which calculation they want to do

choice = input("Please indicate the financial calculations you would like to do : ")

# If user does not enter anything

if  choice == "" :
    print("You have not entered anything ")

# If user choose 'investment' calculation option

elif  choice == "investment" or choice=="INVESTMENT":
    
    # Asking user to enter the amount they  would like to invest
    
    amount = float(input("Please enter the amount that you'll like to invest : "))

    # Asking user to enter the interest rate

    interest_rate = float(input("Please enter the interest rate (e.g '8' without '%' symbol) : "))
    i=interest_rate/100

    # Asking user to enter number of years they want to invest for
    
    years = int(input("Please enter the number of years you plan to invest for : "))

    # Asking user to indicate whether they want to do a simple or compound interest
    
    interest = input("Do you require 'simple' or 'compound' interest : ? ")

    # If user choose to do simple interest,calculate the amount they will get after the investment term they choose

    if(interest == "simple") :
        
        # Simple interest total amount calculation formula
        
        total= amount *(1 + i * years)

        # Displaying Simple interest total interest amount
        
        print(f"Total is : R {total} ")
        
    elif (interest == "compound") :
        
     # If user choose to do compound interest,calculate the amount they will get after the investment term they choose

        # Compound interest total amount calculation formula

        total= amount * math.pow ((1 + i),years)

        # Displaying Compound interest total interest amount
        
        print(f"Total is : R {total} ")
        
# If user choose  to do 'bond' calculation option

elif choice == "bond" or choice=="BOND":
    
     # Asking user to enter the current value of the house
     
     house_value = float(input("Please enter the present value of the house : "))

    # Asking user to enter interest rate
    
     interest_rate = int(input("Please enter the interest rate (e.g '8' without '%' symbol) : "))
     
     # Calculating monthly interest rate
     
     i=interest_rate/100/12

    # Asking user to enter the number of months the user plan to take to repay the bond
    
     months = int(input("Please enter the number of months you plan to take to repay the bond : "))

     # Calculation formula of how much money user will have to repay each month

     monthly_repayment = round((i* house_value  )/( 1-(1 + i)**(-months)),2)

     # Displaying total repayment user will repay each month

     print(f"Total monthly repayment amount for bond is : R {monthly_repayment} ")


    
