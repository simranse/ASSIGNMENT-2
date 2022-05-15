#Question5

a=int(input("Enter first side of a triangle: " ))
b=int(input("Enter second side of a triangle: "))
c=int(input("Enter third side of a triangle: "))
if a+b>c and b+c>a and a+c>b:
    print("No")
else:
    print("Yes")
