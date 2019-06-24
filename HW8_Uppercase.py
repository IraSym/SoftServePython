# Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
# For simplicity, you will not be tested on the ability to handle corner cases (e.g. "%*&#()%&^#" 
# or similar strings containing alphabetical characters at all) - 
# an ALL CAPS (uppercase) string will simply be defined as one containing no lowercase letters. 
# Therefore, according to this definition, strings with no alphabetical characters (like the one above) should return True.

def is_uppercase (char_str):
    boo = char_str.isupper()
    if boo:
        print("All letters are in CAPS")
    else:
        print("Not all letter are in CAPS")

characterString = input("Input character string: ")
is_uppercase(characterString)        