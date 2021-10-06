# simple class with simple method

class Animal:
    def bark(self):
        print("bark")


animal = Animal()
animal.bark()


class pet:
    def bark(self):
        print("bark")

    def groom(self):
        print("groom")


Pet = pet()
Pet.bark()
Pet.groom()

"""Here we are using same bark method 2 types and we have 
created those method two times how we can reduce the code for that we have solution inheritance"""
