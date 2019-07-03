# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_str (boo):
    print(boo)
    if boo == True:
        print("Yes")
    else:
        print("No")    

condition = bool(input("Input condition: "))
bool_str(condition)

