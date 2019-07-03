# Consider an array of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).
# Hint: Don't forget to check for bad values like null/undefined

def count(sheep):
    quantity = sheep.count(True)
    print("The number of sheep is ", quantity)

array = list(input("Input array of sheep as True and False: "))

count(array)
