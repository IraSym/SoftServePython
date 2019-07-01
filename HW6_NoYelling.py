# Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. Using re and string is not allowed.

string = input("Input string (witn uppercase and lowwercase letter): ")

def NoYelling (str):
    string_new = ""
    if str[0].isupper():
        string_new += str[0]
    else:
        string_new += str[0].upper()
    for i in range(1, len(str)):
        string_new += str[i].lower()
    print("New string is: {}".format(string_new))

NoYelling(string)

  
