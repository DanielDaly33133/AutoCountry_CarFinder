#AutoCountry CarFinder App
#Approved Vehilcle List
allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#Menu w/ Options
def menu():
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')
    print("Please Enter the following number below from the following menu: ")
    print("1. Show all Authorized Vehicles")
    print("2. Exit")

menu()
option = int(input("Please Enter the following number below from the following menu: "))

# Menu Options Parameters

#While loop
while option != 2:    
    if option == 1:  
        print(allowedVehiclesList)
    else:
        print('That is not a valid option, please try again.')
    print()
    menu()
    option = int(input("Please Enter the following number below from the following menu: "))


print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')