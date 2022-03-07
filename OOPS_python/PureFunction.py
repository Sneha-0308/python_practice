class Time:
    pass


t1 = Time()
t2 = Time()
t1.h =t1.m =t1.s = 0
t2.h =t2.m =t2.s = 0
start = Time()
start.h = 9
start.m = 45
start.s = 0
duration = Time()
duration.h = 1
duration.m = 35
duration.s = 0


# Pure function
def add_time(t1, t2):
    sum = Time()
    sum.h = t1.h + t2.h
    sum.m = t1.m + t2.m
    sum.s = t1.s + t2.s
    if sum.s >= 60:
        sum.s -=60
        sum.m+=1
    if sum.m>=60:
        sum.m -= 60
        sum.h +=1
    return sum


def print_time(sum):
    print('(%.2d : %.2d : %.2d)' %(sum.h,sum.m,sum.s))


done = add_time(start,duration)
print_time(done)