def modelA(yearsOwned):
    overall_Cost = 16500 + (250 * yearsOwned) + yearsOwned * (MILES_DRIVEN_PER_YEAR/25) * PRICE_OF_GAS
    return overall_Cost

def modelB(yearsOwned):
    overall_Cost = 24500 + (450 * yearsOwned) + yearsOwned * (MILES_DRIVEN_PER_YEAR/40) * PRICE_OF_GAS
    return overall_Cost

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
    
PRICE_OF_GAS = 3
MILES_DRIVEN_PER_YEAR = 40000
choice = input("Would you like estimates for Model A or Model B? (A / B): ").lower()
number_of_estimates = int(input("How many estimate costs would you like to look at?: "))
stringHolder = []
i = 0

if choice == "a":
    while i < number_of_estimates:
        outputting_modelA()
elif choice == "b":
    while i < number_of_estimates:
        outputting_modelB()

for string in stringHolder:
    print(string)
