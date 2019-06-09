# You need to write a function that reverses the words in a given string. 
# A word can also fit an empty string. As the input may have trailing spaces, 
# you will also need to ignore unneccesary whitespace.
line=input("Input sentence: ")
line_list=line.split()
#print(line_list)
line_rev=line_list[::-1]
print(line_rev)