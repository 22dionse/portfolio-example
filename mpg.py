#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()
while True:
    
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    gallons_cost = float(input("Enter cost of gallons:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    if gallons_cost <=0:
        print("Gallons cost nust be greater than zero. Please try again")
        
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_gallons_cost = round((gallons_used * gallons_cost), 1)
        miles_per_gallon = round((miles_driven / total_gallons_cost), 1)
        cost_per_mile = round((miles_per_gallon * gallons_used), 1)

        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gallons_cost    ) 
        print("Cost Per Mile:            ", cost_per_mile   ) 
    choice = input("Get entries for another trip? (y/n)")
    if choice == "n":
        break
print()
print("Bye")



