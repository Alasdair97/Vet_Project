from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes
    age = None
    name = None
    health = None
    weight = None
    
    #Constructors
    def __init__(self):
        self.value = "Animal"


    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        return ("I am sleeping")

    def type(self):
        pass

    def grow(self):
        return ("I am growing")

##################### Mammal 

class Mammal(Animal):
    #Attributes


    #Constructors
    def __init__(self):
        self.value = "Mammal"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        return "Live Birth"

    def type(self):
        pass

################### Bird 

class Bird(Animal):
    #Attributes
    wingspan = None

    #Constructors
    def __init__(self):
        self.value = "Bird"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        return "Lay Egg"


    def type(self):
        pass

########################### Mammals ##########################
    
## Cat
        
class Cat(Mammal):
     #Attributes
    

    #Constructors
    def __init__(self):
        self.value = "Cat"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat mice"

## Dog
        
class Dog(Mammal):
     #Attributes
    breed = None

    #Constructors
    def __init__(self):
        self.value = "Dog"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat meat"

########################### Birds ##########################
    
## Pigeon

class Pigeon(Bird):
     #Attributes
    colour = None

    #Constructors
    def __init__(self):
        self.value = "Pigeon"


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat anythng"
