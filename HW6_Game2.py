# In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. 
# The last person to take a stick wins. Like this:

sticks = 21
sticks = sticks-1
print("Robot take 1 stick. Number of sticks is {}".format(sticks))
while sticks > 0:
    a = int(input("Input number of sticks 1, 2 or 3: ")) # you take a sticks
    sticks = sticks - a
    print("You take {} sticks. Number of sticks is {}".format(a, sticks))
    b = 4 - a           
    sticks = sticks - b                                 # robot take b sticks
    print("Robot take {} sticks. Number of sticks is {}".format(b, sticks))
else:
    print("Robot is the winner!!!")