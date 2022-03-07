class Time:
    pass


t = Time()
t.h = 3
t.m = 30
t.s = 5

def time(t):
    print('(%.2d : %.2d : %.2d )' %(t.h,t.m,t.s))

time(t)
