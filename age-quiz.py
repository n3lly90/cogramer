# Practical Task 
age = int(input("Please enter your age: \n"))

# Use of If- Elif - Else function to print desired outcome
if age > 100:
        print("Sorry, you're dead.")
elif age >= 65:
        print("Enjoy your retirement! \n")
elif age < 13:
        print("You qualify for the kiddie discount! \n")
elif age == 21:
        print("Congrats on your 21st! \n")
else:
        print("Age is but a number. \n")
