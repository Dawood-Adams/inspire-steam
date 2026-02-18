# Name : Dawood Adams
# Date : 17/02/2026
# Program to display diamond using triangles
# write program to display quadratic equation


h = eval(input("Enter diamond's height: "))
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
