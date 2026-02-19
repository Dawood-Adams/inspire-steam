# Name : Dawood Adams
# Date : 19/02/2026
# Program to show objects in python 

class Human:
    # First we define the attributes of a human
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We then create a constructor for this class/object
    # The constructor will be used to create copies of this object
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello I am {self.human_name} and here is a story")
        print("The blacker the berry the sweeter the juice")

# create the humans
dawood = Human("Dawood", 17)
vinicky = Human("Vinicky", 30)

#Let the humans created do things
dawood.tell_story()
print("Dawood's age is", dawood.human_age)

# Modify one of the objects without modifying other objects
vinicky.city = "Kiambu"
print("Vinicky's location", vinicky.city)
print("Dawood's location", dawood.city)