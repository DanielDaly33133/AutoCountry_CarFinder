#AutoCountry CarFinder App v0.2
#Approved Vehilcle List

allowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


#Menu w/ Options
def menu():
    print('********************************')
    print('AutoCountry Vehicle Finder v0.2')
    print('********************************')
    print("Please Enter the following number below from the following menu: ")
    print("1. Show all Authorized Vehicles")
    print("2. Search for Authorized Vehicle")
    print("3. Exit")

menu()
option = int(input("Please Enter the following number below from the following menu: "))

# Menu Options Parameters

#While loop
while option != 3:    
    if option == 1: 
        print(allowedVehiclesList)
    if option == 2:
        response1 = (input('Please Enter the full Vehicle name: ')) 
        for a in allowedVehiclesList:
            if a == response1:
                print(response1 + ' is an authorized vehicle')
                print('********************************')
                print('AutoCountry Vehicle Finder v0.2')
                print('********************************')
                print("Please Enter the following number below from the following menu: ")
                print("1. Show all Authorized Vehicles")
                print("2. Search for Authorized Vehicle")
                print("3. Exit")
                #break or else it marks true response as invalid
                break
                print(menu())
                option = int(input("Please Enter the following number below from the following menu: "))
        else:
            print( response1 + ' is not an authorized vehicle, if you received this in error please check the spelling and try again')
            print(menu())


print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')