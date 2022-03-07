class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print('first name:', self.firstname)
        print('last name: ', self.lastname)


class Student(Person):
    pass


s = Student('mahananda', 'mathdawar')
s.print_name()
p = Person('sneha', 'mathadawar')
p.print_name()
