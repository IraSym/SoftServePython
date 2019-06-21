# Given a string, you have to return a string in which each character 
# (case-sensitive) is repeated once.

def doubling(char):
    char_new=''
    for i in range(0,len(char)):
        char_element = char[i] * 2
        char_new += char_element
    print(char_new)

text = input("Input string: ")
doubling(text)

