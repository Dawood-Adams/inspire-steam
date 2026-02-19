# Name : Dawood Adams
# Date : 19/02/2026
#

def cook_eggs():
    oil = "20ml"
    pan = True
    fire = True
    eggs = 2

    print(f"The pan is {pan},and the fire is {fire},  add {oil} amount of oil and cook {eggs} eggs")

print ("Here is statement 1")

print ("Here is statement 2")

cook_eggs()

print ("here is statement 3")

# Ride fare creating function

def create_fare(route,distance, is_rush_hour):
    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5 
    print(f"The fare on {route} is {fare}")
    return fare
rush_hour = True
returned_fare = create_fare("Juja-Allsops", 7, rush_hour)
print(f"The fare returned is: {returned_fare}")


def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")
    
all_interests = ["Drawing", "Playing Football", "Reading Novels", "Hunting"]

write_all_interests(all_interests)
