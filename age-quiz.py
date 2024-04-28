# Prompt the user to input their age
age = int(input("Please enter your age: \n"))

# Use if-elif-else statements to determine the appropriate message based on the age entered
if age > 100:
    # If age is greater than 100, print a message indicating the person is considered deceased
    print("Sorry, you're dead.")
elif age >= 65:
    # If age is 65 or greater, print a message indicating the person is eligible for retirement
    print("Enjoy your retirement! \n")
elif age < 13:
    # If age is less than 13, print a message indicating the person qualifies for a discount typically given to children
    print("You qualify for the kiddie discount! \n")
elif age == 21:
    # If age is exactly 21, print a message to celebrate the person's 21st birthday
    print("Congrats on your 21st! \n")
else:
    # For any other age, print a generic message
    print("Age is but a number. \n")
