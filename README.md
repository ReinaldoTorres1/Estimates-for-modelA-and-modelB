# Estimates-for-modelA-and-modelB

### Author: Reinaldo Torres
### Created: 10/20/2020
### Gaining Estimate Costs for Two Metaphorical Cars: ModelA and ModelB

# Here we are going to create two definitions. Each of these will take an arguement called "yearsOwned" and use it to compute the overall_cost of owning either Model A or Model B.
# We add "return" to return the output of the formula to whatever called it. (We will be passing arguements into these later)

def modelA(yearsOwned):
    overall_Cost = 16500 + (250 * yearsOwned) + yearsOwned * (MILES_DRIVEN_PER_YEAR/25) * PRICE_OF_GAS
    return overall_Cost
def modelB(yearsOwned):
    overall_Cost = 24500 + (450 * yearsOwned) + yearsOwned * (MILES_DRIVEN_PER_YEAR/40) * PRICE_OF_GAS
    return overall_Cost

# These two modules are to condense the code we do later on. They both do almost the same thing. I originally thought I could have one
# Definition and use that to output either model a or model b to the user. I couldn't figure out how though so I opted for two
# different definitions instead.

def outputting_modelA():
    global i
    yearsOwned = float(input("How many years do you see yourself owning this car?: "))
    holder = "The total cost of owning the ModelA for {} years is: ${}".format(int(yearsOwned), modelA(yearsOwned))
    stringHolder.append(holder)
    i+=1
def outputting_modelB():
    global i
    yearsOwned = float(input("How many years do you see yourself owning this car?: "))
    holder = "The total cost of owning the ModelB for {} years is: ${}".format(int(yearsOwned), modelB(yearsOwned))
    stringHolder.append(holder)
    i+=1

# The price of gas and Miles driven per year were constants in the original math problem I made this algorithm for
# so they are constants within this program as well.

PRICE_OF_GAS = 3
MILES_DRIVEN_PER_YEAR = 40000

# Receive user input for the later decision structure that'll decide which definition (ModelA or ModelB) to use.
# Receive the number of estimates in order to control the while loop later on.

choice = input("Would you like estimates for Model A or Model B? (A / B): ").lower()
number_of_estimates = int(input("How many estimate costs would you like to look at?: "))

# Creating a list to hold variables that contain formated strings we want to print later.
stringHolder = []

# Setting a control variable and creating a decision structure that has a loop structure nested within it.
# We will compare i to number of estimates to ensure we take in and output the exact number of items the user wants.
# We will have a holder variable that'll contain a formated string and multiple of that holder variable will be added to a list for later use.

i = 0
if choice == "a":
    while i < number_of_estimates:
        outputting_modelA()

# An alternative option for the user.
# We will compare i to number of estimates to ensure we take in and output the exact number of items the user wants.
# We will have a holder variable that'll contain a formated string and multiple of that holder variable will be added to a list for later use.

elif choice == "b":
    while i < number_of_estimates:
        outputting_modelB()

# A for loop to print out all elements we added to the stringHolder list earlier.

for string in stringHolder:
    print(string)