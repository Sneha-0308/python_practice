class motor:
    def __init__(self, speed):  # self represents the instance of the class. By using the
        # “self” keyword we can access the attributes and methods of the class in python.
        self.Speed = speed

    def increase_speed(self, increased):
        self.Speed += increased


honda = motor(50)
ducati = motor(50)
honda.increase_speed(50)
ducati.increase_speed(0)
print(honda.Speed)
print(ducati.Speed)
