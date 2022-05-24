# e2100306
# propertydriver

from propertyapp import *

def main():
    # to allow customized color and text modification for user input
    RED     = '\033[31m'
    BOLD    = '\033[1m'
    # # to be able remove the modification color and cosmetics to default text
    RESETCOLOR  = '\033[39m'
    RESET   = '\033[0m'
    # while option equals to 0 allow user to enter number based on their choice
    groupname = input("What's the name of your property company? " + RED + BOLD)  
    print(RESETCOLOR + RESET)
    newPropertyList = PropertyList(groupname)
    option = -1
    while option != 0:
        print (newPropertyList.getgroupname())
        menu()
        option = eval(input("Your choice: " + RED + BOLD))
        print(RESETCOLOR + RESET)
        # option 1 user add property
        if option == 1:
            # user input a location
            location = input("Location: " + RED + BOLD)
            print(RESETCOLOR + RESET)
            # user input price
            price = eval (input("Price: " + RED + BOLD))
            print(RESETCOLOR + RESET)
            # user input type of property
            propertyType = input("Property type ('A'partmen, 'B'ungalow, 'C'ondominium) : " + RED + BOLD)
            print(RESETCOLOR + RESET)
                # to display the type of property user choses
            Size = eval(input("in square feet, eg. 1438: " + RED + BOLD))
            print(RESETCOLOR + RESET)
            newProperty = property(location, price, propertyType, Size)
            newPropertyList.addProperty(newProperty)
            # print("Adding a new property" )
            print(str(newProperty) + " ... added succesfully.")

        # option 2 to display all properties 
        elif option == 2:
            # display when no property that have been registered
            if(newPropertyList.noOfProperties == 0):
                print("No property has been registered yet")
            # if registered
            else:
                print(newPropertyList.allProperties())

        # option 3 to see summary of registered and number
        elif option == 3:
            # prints summary info how many property user have
            print("Summary Information")
            print("Number of registered properties: " + str(newPropertyList.noOfProperties()))
            print("Total price: " + str(newPropertyList.totalPrice()))
            print("Most Expensive: " + str(newPropertyList.mostExpensiveProperty()))
            


        # option 4 to display property with types
        elif option == 4:
            # to be able see how many type of property
            amount = newPropertyList.noOfProperties()
            # typeproperty = 
            if(amount == 0):
                print("No property has been registered yet")            
            else:
                typeproperty = input("property type ('A'partment, 'B'ungalow, 'C'ondomonium): " + RED + BOLD)
                print(RESETCOLOR + RESET)
                print("the properties are: " )
                i = newPropertyList.getpropertycollection()
                # to find type of property
                if typeproperty == "A" or typeproperty == "a":
                    for i in newPropertyList.findPropertyByType("apartment"):
                        print(str(i))

                if typeproperty == "B" or typeproperty == "b":
                    for i in newPropertyList.findPropertyByType("bungalow"):
                        print(str(i))

                if typeproperty == "C" or typeproperty == "c":
                    for i in newPropertyList.findPropertyByType("condomonium"):
                        print(str(i))
                        
        # option 5 to sell property
        elif option == 5:
            amount = newPropertyList.noOfProperties()
            if(amount == 0):
                print("No property has been registered yet")
            else:
                indexproperty = eval(input("Property to sell (1.." + str(amount) + ")? " + RED + BOLD))
                print(RESETCOLOR + RESET)
                # if user input 0 or less amount property user have
                if (indexproperty <= 0 or indexproperty > amount):
                    print("Out of range...")
                # user put number as they wish to sell their property
                else:  
                    print(str(newPropertyList.getpropertycollection()[indexproperty-1]))
                    newPropertyList.sellProperty(indexproperty)
                    print("has been sold.")
                
        # option 6 to sort properties
        elif option == 6:
            # property won't show if none have registered
            amount = newPropertyList.noOfProperties()
            if(amount == 0):
                print("No property has been registered yet")
            else:
                # user input the criteria
                sort = input("criteria (price, tax, or size) ? " + RED + BOLD)
                print(RESETCOLOR + RESET)
                # sort = "price", "tax", "size"
                i = (newPropertyList.allProperties())
                if sort == "price".lower():
                    for i in newPropertyList.sortedProperty("price"):
                        print(str(i))

                if sort == "tax".lower():
                    for i in newPropertyList.sortedProperty("tax"):
                        print(str(i) + " with annual tax $" + str(newProperty.annualtax()))

                if sort == "size".lower():
                    for i in newPropertyList.sortedProperty("size"):
                        print(str(i))

        # option 7 to load data from file that being made
        elif option == 7:
            filename = input("File name to load from: " + RED + BOLD)
            print(RESETCOLOR + RESET)
            newPropertyList.loadfromfile(filename)

        # option 8 to save file
        elif option == 8:
            filename = input("File name to save to: " + RED + BOLD)
            print(RESETCOLOR + RESET)
            newPropertyList.savetofile(filename)
            
        # else 0 to quit
        else:
            print("sayonara...")

def menu():
    print("--------------------------")
    print("1 Add a property")
    print("2 Display all properties")
    print("3 Display summary information about property")
    print("4 Display properties based on given index")
    print("5 Sell a property based on given index")
    print("6 Display all properties, sorted according to Property values")
    print("7 Read properties information from file")
    print("8 Write properties information to file")

    print("0 quit")
main()
