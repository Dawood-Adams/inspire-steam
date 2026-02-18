# Name : Dawood Adams
# Date : 17/02/2026
# Program to format the output in different types

name = 'Dawood Adams'
weight = 76
favourite_team = 'RB Leipzig'
height = 178
#1.Format using print(f"{}")

print(f"My name is {name} and I weigh {weight} kg.")

#2.using f string
msg = f"My name is {name} and I support {favourite_team}."
print(msg)

#3.using {} and  .format()

print("My name is {0} and I am {1} cm tall.".format(name,height))

#4.using output specifies like %s
import math
print("The value of pi is approximately %5.3f." % math.pi)

#%f is for float fractions
print("I support %s" %favourite_team)