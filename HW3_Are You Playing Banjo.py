# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.
name=input("Input your name: ")
if name[0] == "R" or name[0] == "r":
    print("{} plays banjo".format(name))
else:
    print("{} does not play banjo".format(name))
    
