#CarFinder
#This program allows a user to find allowed vehicles.

AllowedVehiclesList = ['Ford F-150' , 'Chevrolet Silverado' , 'Tesla Cybertruck' , 'Toyota Tundra' , 'Nissan Titan']

#Adding the menu.
def print_menu():
    print('********************************')
    print('AutoCountry Vehicle Finder v0.1')
    print('********************************')
    print('Please Enter the following number below from the following menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. Exit')

#Adding second part of the menu.
def print_allowed_vehicles_list():
    print('\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicles in AllowedVehiclesList:
        print(vehicles)
    menu = f"""
The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:
{print_allowed_vehicles_list}
*******************************
AutoCountry Vehicle Finder v0.1
*******************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. Exit
"""
#
def main():
    while True:
        print_menu()
        option = input()
        if option == '1':
            print_allowed_vehicles_list()
        elif option == '2':
            print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()