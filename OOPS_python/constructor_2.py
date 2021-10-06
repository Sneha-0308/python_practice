class Motor:
    def __init__(self, speed):
        print(speed)
        print("Motor class instance is created")


honda = Motor(50)
ducati = Motor(100)
# print(honda.speed)
# print(ducati.speed)
""" this two line we will get error because we did not created any attribute
 called speed in the  constructor . if you want to print the value outside that
  constructor we have to create attribute in that constructor using self keyword
  check in the constructor3.py file"""
