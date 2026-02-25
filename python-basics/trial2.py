'''
we\ll create a function to cook eggs, 
and a function to only accept students with a certain SAT score
'''


def cook_eggs(eggs_to_use, add_salt, egg_price=15):
    egg_price2 = str(int(egg_price)) + " shillings"
    print(f"I want to cook {eggs_to_use} eggs with {add_salt} and it is {egg_price2}")
    for x in range(0,eggs_to_use):
        print("Here is an egg to use")
    print(f"The total number of eggs is {eggs_to_use}")#An egg should be 15 shillings and the total cost of all eggs should be given
    print(f"The total price of the eggs will be {eggs_to_use * egg_price} shillings")

cook_eggs(50,"20 grams",15)
