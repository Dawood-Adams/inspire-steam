# Name : Dawood Adams
# Date : 16/02/2026
# Program to calculate factorials of numbers

number = int(input("Enter the number"))

factorial = 1 # Initiate factorial
for x in range(1,number+1):
    factorial *= x
    
print(f"{number}!={factorial}")
