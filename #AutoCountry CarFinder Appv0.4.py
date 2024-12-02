#AutoCountry CarFinder App v0.4
#Approved Vehilcle List


allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]

#Menu w/ Options
def menu():
    print('********************************')
    print('AutoCountry Vehicle Finder v0.4')
    print('********************************')
    print("Please Enter the following number below from the following menu: ")
    print("1. Show all Authorized Vehicles")
    print("2. Search for Authorized Vehicle")
    print("3. ADD authorized vehicle")
    print("4. REMOVE authorized vehicle")
    print("5. Exit")

    

menu()
option = int(input("Please Enter the following number below from the following menu: "))

# Menu Options Parameters

#While loop
while option != 5:    
    if option == 1: 
        print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ')
        print(allowedVehiclesList)
        print(menu())
        option = int(input("Please Enter the following number below from the following menu: "))
    if option == 2:
        response1 = (input('Please Enter the full Vehicle name: ')) 
        for a in allowedVehiclesList:
            if a == response1:
                print(response1 + ' is an authorized vehicle')
                print('********************************')
                print('AutoCountry Vehicle Finder v0.4')
                print('********************************')
                print("Please Enter the following number below from the following menu: ")
                print("1. Show all Authorized Vehicles")
                print("2. Search for Authorized Vehicle")
                print("3. Exit")
                #break or else it marks true response as invalid
                break
                print(menu())
                option = int(input("Please Enter the following number below from the following menu: "))
    
    if option == 3:
        print(menu())
        response2 = input('Please Enter the FULL NAME of the vehicle you would like to ADD: ')
        allowedVehiclesList.append(response2)
        print("You have added " + (response2) + " as an authorized vehicle")
        print(menu())
        option = int(input("Please Enter the following number below from the following menu: "))

    if option == 4:
        print(menu())
        response3 = input('Please Enter FULL NAME of the vehicle you would like to REMOVE: ')
        response4 = int(input('Are you sure you want to REMOVE ' + (response3) + ' from authorized vehicles? Choose 1.Yes or 2.No: '))  
        if response4 == 1:
            allowedVehiclesList.remove(response3)
            print('You have removed ' + (response3) + ' as an authorized vehicle')
            print(menu())
            option = int(input("Please Enter the following number below from the following menu: "))
        else:
            print(menu())
            option = int(input("Please Enter the following number below from the following menu: "))

    else:
        print( response1 + ' is not an authorized vehicle, if you received this in error please check the spelling and try again')
        break
            
print(menu())
option = int(input("Please Enter the following number below from the following menu: "))   


print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')