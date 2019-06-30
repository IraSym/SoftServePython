# Given two ordered pairs calculate the distance between them. Round to two decimal places. 
# This should be easy to do in 0(1) timing.

a1 = float(input("Input the element a[1]: "))
a2 = float(input("Input the element a[2]: "))
b1 = float(input("Input the element b[1]: "))
b2 = float(input("Input the element b[2]: ")) 
dist = round(((a1-b1) ** 2 + (a2-b2) ** 2) ** (0.5), 2)
print("Distance between a and b is {}".format(dist))


