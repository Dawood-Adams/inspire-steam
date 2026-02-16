# Name : Dawood Adams
# Date : 12/02/2026
# Program to calculate arithmetic progression

#calculating the nth term

a = int(input("Enter the first number :"))
n = int(input("Enter the number of terms :"))
d = int(input("Enter the common difference :"))
r = int(input("Enter the common ratio :"))

nth_term = a + (n - 1) * d
print(f"The nth term is :{nth_term}")

Sn = (n/2) * (2*a+(n - 1)*d)
print(f"The sum of the numbers in the sequence is :{Sn}")

nth_term2 = a * (r**(n - 1))
print(f"The nth term of the Geometric progression is:{nth_term2}")
# calculating the Geometric progression