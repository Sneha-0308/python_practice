class Modifiers:
    pass


time = Modifiers()
time.h = 9
time.m = 50
time.s = 10


# Writing modifier function
def increment(time, incsec):
    time.s += incsec
    if time.s >= 60:
        time.s = 60
        time.m += 1

    if time.m >= 60:
        time.m -= 60
        time.h += 1

    return time


def print_time(inc):
    print('(%.2d : %.2d : %.2d)' %(inc.h,inc.m,inc.s))


done =increment(time,70)
print_time(done)