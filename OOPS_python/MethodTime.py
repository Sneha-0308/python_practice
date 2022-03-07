# class Time:
#     def print_time(time):
#         print('(%.2d : %.2d : %.2d)' %(time.h,time.m,time.s))
#
# t = Time()
# t.h = 0
# t.m = 0
# t.s = 0

"""Class_name.method(object)
OR WE CAN USE
object.method()"""

# Time.print_time(t)
# t.print_time()


class Time:
    def print_time(self):
        print('(%.2d : %.2d : %.2d)' %(self.h,self.m,self.s))


t = Time()
t.h = 10
t.m = 5
t.s = 12
Time.print_time(t)