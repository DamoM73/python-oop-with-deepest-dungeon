# main.py

from pet import Pet
from shelter import Shelter

# create shelter
shelter = Shelter("Happy Paws")

# add pets
shelter.add_pet(Pet("Rex", 3))
shelter.add_pet(Pet("Mittens", 2))

shelter.list_pets()
