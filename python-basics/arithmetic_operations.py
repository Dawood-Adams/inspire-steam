# Name : Dawood Adams
# Date : 17/02/2026
# Program to perform arithmetic operations

first_number = 12
second_number = 34
sum_numbers = first_number + second_number
difference_numbers = first_number - second_number
product_numbers = first_number * second_number
quotient_numbers = first_number / second_number

print("The sum of the numbers %d" %sum_numbers)
print("The difference of the numbers %d" %difference_numbers)
print("The product of the numbers %d" %product_numbers)
print("The quotient of the numbers %0.4f" %quotient_numbers)

# modulus/remainder
print(7%5)
# Even and Odd numbers
for x in range(0,21):
    if (x%2 ==0):
        print(f"{x} is even number")
    elif(x%2 ==1):
        print(f"{x} is odd number")