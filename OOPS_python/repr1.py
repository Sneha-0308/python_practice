class Repr1:
    def __init__(self, USN, NAME):
        self.usn = USN
        self.name = NAME

    def __repr__(self):
        return repr((self.usn, self.name))


"""__repr__ ::The __repr__ method returns the string representation 
of an object. Typically, you returns a string so that if you execute 
it as a statement, it would return the object.
 Syntax : def __repr__(self):
              return repr((self........))"""

print(Repr1("2ke19cs104", "Sneha"))
