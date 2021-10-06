""""__init__" is a reseved method in python classes.
It is known as a constructor in object oriented concepts.
 This method called when an object is created from the class
 and it allow the class to initialize the attributes of a class. """


class Motor_Bike:
    def __init__(self, name="ruby"):  # default value
        print(name)
        self.speed = 50
        self.naam = name


honda=Motor_Bike("sneha")
print(honda.speed)
print(honda.naam)