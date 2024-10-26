#CarFinder
#This program allows a user to find allowed vehicles.

AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Titan']

#Adding the menu.
def print_menu():
    menu = f"""
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. Print all Authorized Vehicles
2. Exit
"""
    print(menu)