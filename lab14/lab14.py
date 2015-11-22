class PetError(Exception):
    pass

class Pet(object):
    def __init__(self,species = None,name = ''):
        if species != 'dog':
            if species != 'cat':
                if species != 'horse':
                    if species != 'gerbil':
                        if species != 'hamster':
                            if species != 'ferret':
                                if species != 'bird':
                                    if species != '':
                                        raise PetError("Not the right pet")
        self.name = name
        self.species = species
        
    def __str__(self):
        if self.name:
            return "Species of: %s,named %s" % (self.species, self.name)
        else:
            return "Species of: %s,unnamed" % (self.species)

class Dog(Pet):
    def __init__(self,name='',chases='Cats'):
        Pet.__init__(self,"dog",name)
        self.chases = chases
    def __str__(self):
        common_str = Pet.__str__(self)
        other_str = common_str + " who chases %s" % (self.chases)
        return other_str


class Cat(Pet):
    def __init__(self,name='',hates='Dogs'):
        Pet.__init__(self,"cat",name)
        self.hates = hates
    def __str__(self):
        common_str = Pet.__str__(self)
        other_str = common_str + " who hates %s" % (self.hates)
        return other_str


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

demo()


