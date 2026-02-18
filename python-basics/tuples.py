# Name : Dawood Adams
# Date : 18/02/2026
# Program to show tuples in python

fruits = ("Avocado","Kiwi","Apples","Bananas","Orange")
print(len(fruits))
print(fruits[0])
print(fruits[4])
print(fruits[-1])
print(fruits[-5])
# error ->fruits.append("Guava")

fruits_list = list(fruits)
print(fruits_list)
fruits_list.append("Guava")
print(fruits_list)
new_fruits = tuple(fruits_list)
print(new_fruits)
print(new_fruits[5])
