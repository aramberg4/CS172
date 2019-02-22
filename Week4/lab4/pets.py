#File Name:  pets.py
#Purpose:    Test the mammals, dog and cat classes
#Author:     Adelaida A. Medlock
#Date:       January 28, 2019

from mammals import Mammal
from dog import Dog
from cat import Cat

def main():
    # Create an Mammal object, a Dog object, and a Cat object
    mammal = Mammal('generic animal', 2)
    dog = Dog(3, 'beagle')
    cat = Cat(5)

    # Display information about each one.
    print('Here are some animals and the sounds they make')
    print('----------------------------------------------')
    showMammalInfo(mammal)
    print()
    showMammalInfo(dog)
    print()
    showMammalInfo(cat)
    print()
    showMammalInfo('Apple Tree')


# The show_mammal_info function accepts an object
# as an argument, and calls its show_species
# and make_sound methods.
def showMammalInfo(creature):
    if isinstance(creature, Mammal):
        print(creature)
        creature.makeSound()
    else:
        print('That is not a Mammal!')

# Call the main function.
main()