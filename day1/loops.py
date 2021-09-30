# for loop
# range (value(including), value(excluding))
# example range(1,10) this range will include 1 up to 9
# Syntax of for loop:= for variable in range(value1, value2):
for i in range(1, 10):
    print(i)

# print sum of first n natural number
n = 5
sum = 0
for j in range(1, n+1):
    sum = sum+j
print(sum)

# multiplication table

value = 2
for i in range(1, 11):
    res = value*i
    print(f"{value}*{i}={res}")

# here we will use another way to print

# value=2
# for i in range(1, 11):
#     res=value*i
#     print("{0}*{1}={2}".format(value, i, res))

# how to print odd number and even numbers
# ODD NUMBERS
# (val1, val2, step) ==>Syntax
for i in range(1, 11, 2):
    print(i)

# EVEN NUMBERS
for i in range(0, 11, 2):
    print(i)

# HOW TO PRINT NUMBERS IN REVERSE
for i in range(10, 0, -1):
    print(i)
