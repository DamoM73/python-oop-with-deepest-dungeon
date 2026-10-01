# shelter.py

class Shelter():

    def __init__(self, name):
        # initialises the shelter object
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        # adds a pet to the shelter
        self.pets.append(pet)

    def list_pets(self):
        # displays every pet that hasn't been adopted
        print(f"\nPets at {self.name}:")
        for pet in self.pets:
            if not pet.adopted:
                pet.describe()

    def adopt(self, pet_name):
        # adopts the pet with the given name, if it's available
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower() and not pet.adopted:
                pet.adopted = True
                return pet
        return None
