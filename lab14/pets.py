# add your class definitions here


def demo():
    try:
        pet = Pet('horse')
        print(pet)   # -->
        dog = Dog('fido')
        print(dog)   # --> species of Dog, named fido who chases Cats
        cat = Cat('fluffy', 'everything')
        print(cat)   # --> species of Cat, named fluffy who hates everything
        pet = Pet('pig')   # raises a PetError
        print(pet)   
    except PetError:
        print("Got a pet error.")   # --> Got a pet error
