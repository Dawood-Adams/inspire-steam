# Name : Dawood Adams
# Date : 23/02/2026
# Program to show classes in python

class Car():
    # Attributes of the car
    def __init__(self,make,model,color,year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year

#print car details
    def print_details(self,make,model,color,year):
        print(f"Car details: {make} {model} of color {color} was made in the year {year}")

#Instantiate a class object

my_car = Car("Mazda","Atenza","Dark Grey",2022)
dads_car = Car("Nissan","Patrol","Black",2024)

my_car.print_details("Mazda","Atenza","Dark Grey",2022)

