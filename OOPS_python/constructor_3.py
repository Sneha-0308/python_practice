class Motor:
    def __init__(self, speed):
        print(speed)
        self.velocity = speed
        """ syntax: self.attribute_name = attribute 
        here attribute_name is something which will be used in outside the constructor to print
        And attribute is variable which is same as the variable name passed in __init__ Method so 
        self.attribute_name = attribute is used to assign value to attribute_name  """
        # print("Motor instance is created")


honda = Motor(50)
ducati = Motor(100)
print(honda.velocity)
print(ducati.velocity)