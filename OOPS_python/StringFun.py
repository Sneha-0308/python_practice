class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return '%.2d : %.2d : %.2d' % (self.h, self.m, self.s)


t = Time(9)
# when print() or str() function are invoked that time it calls __str__(self) method automatically
print(t)

