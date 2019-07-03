# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails.
# To help her, you must correct the broken function to make sure that the second argument (tail), 
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false. The arguments will always be strings, and normal letters.
# For Haskell, more specifically, body has the type of String and tail has the type of Char.

def true_tail (animal, tail):
    if animal[-1] == tail:
        print(animal, tail, True)
    else:
        print(animal, tail, False)

name = input("Input name of animal: ")
name_tail = input("Input letter for tail: ")

true_tail(name, name_tail)
    