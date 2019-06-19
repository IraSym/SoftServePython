# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.

def summ (num):
    s=0
    for i in range(1,num+1):
        s += i
    print("Sum = ", s)

number=int(input("Input positive integer: "))
summ(number)