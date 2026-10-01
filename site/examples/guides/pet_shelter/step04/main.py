# main.py

from pet import Dog, Cat
from shelter import Shelter

# create shelter
shelter = Shelter("Happy Paws")

# add pets
shelter.add_pet(Dog("Rex", 3))
shelter.add_pet(Cat("Mittens", 2))
shelter.add_pet(Dog("Biscuit", 5))

# ----- MAIN LOOP -----
running = True
while running:
    command = input("\nlist, adopt or quit? > ").lower()

    if command == "list":
        shelter.list_pets()
    elif command == "adopt":
        choice = input("Which pet? > ")
        pet = shelter.adopt(choice)
        if pet:
            print(f"You adopted {pet.name}!")
            pet.speak()
        else:
            print(f"{choice} isn't available.")
    elif command == "quit":
        running = False
    else:
        print("Please type list, adopt or quit.")

print("Thanks for visiting Happy Paws.")
