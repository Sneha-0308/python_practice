# class Animal:
#     def bark(self):
#         print("bark")
#
#
# animal = Animal()
# animal.bark()
#
#
# class pet:
#     def bark(self):
#         print("bark")
#
#     def groom(self):
#         print("groom")
#
#
# Pet = pet()
# Pet.bark()
# Pet.groom()

class Animal:
    def bark(self):
        print("bark")


class Pet(Animal):  # this how we can inherit the class
    def groom(self):
        print("groom")


pet = Pet()
pet.bark()
pet.groom()