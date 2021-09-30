print("Hello")
print("5*2=10")
print(5*2)
print('sneha')
print("hello\nsneha")
print("hello\tsneha")
# the absolute value is always a positive value and not a negative number.
# If the number is positive then it will result in a positive number only.
print(abs(10.5))
print(abs(-40))
print(abs(3-4j)) # abs for complex number it gives magnitude
# abs() only stores the numbers not strings

print(pow(2, 5)) # pow() power function
print(max(1, 2, 3)) # max() maximum function
print(min(1, 2, 3, 4)) # min() minimum function

# print statement
# print("statement {index}".format(operation))
print("value\t{0}".format(5*2))
print("sum={0}".format(4+4))
print("{0}*{1}={2}".format(4, 4, 4*4)) # at index 0=4, at index 1=4, index 2=4*4=16
print("My name is {0}".format("Sneha", "Mana"))
# adding three numbers
a = 5
b = 2
c = 4
print("{0}+{1}+{2}={3}".format(a, b, c, a+b+c))

# Another way to print statement
# print(f"statement {operand}")
x = 1
print(f"value of x is {x} ")
y = 2
z = 3
sum = x+y+z
print(f"{x}+{y}+{z}={sum}")

# NORMAL DIVISION :Divides the value on the left by the one on the right.
# Notice that division results in a floating-point value.
print(5/2)

# FLOOR DIVISION : Divides and returns the integer value of the quotient.
# It neglects the digits after the decimal.
print(5//2)

# ROUND OFF NUMBERS
# WORKING OF ROUND() METHOD: The round () method returns a floating-point number, rounded
# to the specified number of the decimal point. number: The number to be rounded off.
# digits: (Optional) The number of digits to round off. Defaults to 0.
print(round(2.33333, 1))
print(round(2.33333))  # round(value, default=0)

# TYPE CASTING
print(int(3.44))
print(float(3))
i = 10
print(i < 5)  # BOOLEAN DATATYPE
print(i==10)
