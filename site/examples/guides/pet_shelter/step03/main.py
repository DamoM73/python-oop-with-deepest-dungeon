# main.py

from pet import Dog, Cat
from shelter import Shelter

# create shelter
shelter = Shelter("Happy Paws")

# add pets
shelter.add_pet(Dog("Rex", 3))
shelter.add_pet(Cat("Mittens", 2))

shelter.list_pets()

# test the sounds
for pet in shelter.pets:
    pet.speak()
