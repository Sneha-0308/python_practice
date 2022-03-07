class Initialization:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def print_time(self):
        print('(%.2d : %.2d : %.2d)' %(self.h,self.m,self.s))


t = Initialization(9)
t.print_time()