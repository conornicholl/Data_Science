import math

# Output intro message and user options
print("Financial Calculator")
print('''Investment - To calculate the amount of interest
       you'll earn on your investment''')
print("Bond - To calculate you'll have to pay on a home loan")
print(" ")

# Prompt user to enter eith 'investment' or 'bond'
selection = input("Enter either 'Investment' or 'Bond' to proceed: " ).lower()


# Handling 'investment' option
if selection == "investment":

    # Get user details
    money = float(input("How much money are you investing? "))
    rate = float(input("What is the interest rate?(%)" ))
    years = int(input("How many years do you want to invest? "))

    # Ask user for interest input
    investment = input("Do you want simple or compound interest? ").lower()

    # Calculate simple interest, to 2 decimal places
    simple_interest = round(money * (1 + rate/100 * years), 2)

    # Calculate compund interest, to 2 decimal places
    compound_interest = round(money * math.pow((1 + rate/100), years), 2)


    # Display simple interest
    if investment == "simple":
        print("Your simple interest is: " + str(simple_interest))
    

    # Display compound interest
    elif investment == "compound":
        print("Your compound interest is: " + str(compound_interest))

# Handling the 'bond' option
elif selection == "bond":

    # Get user's bond details
    value = float(input("What is the current value of your house? "))
    rate = float(input("What is the current rate?(%) "))
    months = int(input("Within how many months do you want to repay the bond? "))
    monthly_rate = ((rate/100)/12)

    # Calculate month repayment, round to 2 decimal places
    bond_repayment = round((monthly_rate * value) 
                           / (1-(1 + monthly_rate) 
                            ** (- months)), 2)

    # Print user's monthly repayment
    print("Your monthly repayment will be: " + str(bond_repayment))

# Print error message if user inputs neither investment or bond
else:
    print("ERROR - Please enter a valid selection")
