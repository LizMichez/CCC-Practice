# This program calculates the coins needed to make change

money = int(input("Input change in cents (less than 1$): "))  # Declares var money as an integer based on user input

quarters = 0  # Declares var quarters as 0
dimes = 0  # Declares var dimes as 0
nickels = 0  # Declares var nickles as 0
pennies = 0  # Declares var pennies as 0

while money > 0:  # Opens while loop
    if money > 25:  # If the number is greater than 25
        quarters = quarters + 1  # Increase quarters by 1
        money = money - 25  # Decrease money by 25
    elif money > 10:  # If the number is greater than 10
        dimes = dimes + 1  # Increase dimes by 1
        money = money - 10  # Decrease money by 10
    elif money > 5:  # If the number is greater than 5
        nickles = nickles + 1  # Increase nickles by 1
        money = money - 5  # Decrease money by 5
    else:  # If the number meets none of the previous conditions
        pennies = money  # Set pennies to money
        money = 0  # Sets money to 0

print("Your change is", quarters, "quarters,", dimes, "dimes,", nickels, "nickels, and", pennies, "pennies.")
# The line above prints the total change breakdown
