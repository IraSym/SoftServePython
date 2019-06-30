# In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. 
# The last person to take a stick wins. Like this:

sticks=21
Name1=input("Input name of the first player: ")
Name2=input("Inpur name of the second player: ")
Name=Name1
Boo=True
while sticks > 3:
    a = int(input("{}, Please input number of sticks 1, 2 or 3: ".format(Name)))
    sticks = sticks - a
    Boo = not Boo
    if Boo == True:
        Name=Name1
    else: 
        Name=Name2
else:      
    print=("The winner is {}!!!".format(Name))