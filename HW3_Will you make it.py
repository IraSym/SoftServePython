# You were camping with your friends far away from home, but when it's time to go back, 
# you realize that you fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. 
# Considering these factors, write a function that tells you if it is possible to get to the pump or not. 
# Function should return true if it is possible and false if not.
fuel=float(input("Input how many gallons of fuel is available: "))
distance=float(input("Input how many miles to the  nearset pump: "))
if fuel*25 > distance:
    print("It is POSSIBLE to get to the pump!!!")
else: 
    print("It is IMPOSSIBLE to get to the pump!!!")
print("Be careful on the road!!!")