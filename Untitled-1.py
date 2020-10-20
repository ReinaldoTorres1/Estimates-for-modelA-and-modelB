def is_it_palindrome(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_it_palindrome(string[1:-1])
        else:
            return False

# user_input = str(input("enter a string: "))
# if(is_it_palindrome(user_input)==True):
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")


# list = ['jessy','archy','jessica','fransis','hanzo','hess','fresno','jen','crafto']

# anotherlist = list[1:-1]
# yetanotherlist = anotherlist[1:-1]
# andyetanotherlist = yetanotherlist[1:-1]
# print(list[:-1])
# print(list[-1:])
# print(anotherlist)
# print(anotherlist[1:-1])
# print(yetanotherlist[1:-1])
# print(andyetanotherlist[1:-1])

# list5 = ['franco']
# print(len(list5))

def modelA(yearsOwned, Price_of_Gas):
    modelA = 16500 + (250 * yearsOwned) + yearsOwned * (40000/25) * Price_of_Gas
    print(modelA)

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

# cars = []

# x = int(input("How many cars would you like to input?: "))
# j = 0 
# while j < x:
#     color = input("color: ")
#     model = input("model: ")
#     cars.append(Car(color, model))
#     j +=1 

# for car in cars:
#     print(car.color, car.model)
# p1 = Person("Johnny", 24)
# print(p1.color)
# print(p1.model)


# i = int(input("How many cars would you like to input?: "))

# x = 0
# while x < i:
#     color = input("Color: ")
#     looks = input("Looks like: ")
#     car = Car(color, looks)
#     cars.append(car)
#     x += 1
# print(car[0])







# class Carz:
#     def __init__(self, color, make):
#         self.color = color
#         self.make = make
    
#     def __repr__(self):
#         return "This cars color is %s, and its make is %s" % (self.color, self.make)

# t = Carz("blue", "honda")
# print(t)

# class Car:
#     def __init__(self, cost, gas_mileage, insurance_per_year):
#         self.cost = cost
#         self.gas_mileage = gas_mileage
#         self.insurance_per_year = insurance_per_year
    
    # def __repr__(self):
    #     return "This car costs %d and has a gas mileage of %d" % (self.cost, self.gas_mileage)


# Here we are going to create two definitions. Each of these will take an arguement and use it to compute the overall_cost of owning either Model A or Model B.
# We add "return" to return the output of the formula to whatever called it. (We will be passing arguements into these later)
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

# estimates, stringHolder = ([], ) * 2

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
# We will have a holder variable that'll contain a formated string and that holder variable will be added to a list for later use.
i = 0
if choice == "a":
    while i < number_of_estimates:
        outputting_modelA()
# An alternative option for the user.
# We will compare i to number of estimates to ensure we take in and output the exact number of items the user wants.
# We will have a holder variable that'll contain a formated string and that holder variable will be added to a list for later use.
elif choice == "b":
    while i < number_of_estimates:
        outputting_modelB()

# A for loop to print out all elements we added to the stringHolder list earlier.
for string in stringHolder:
    print(string)