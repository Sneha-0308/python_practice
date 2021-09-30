# PYTHON METHOD
# SYNTAX FOR METHODS
# def method_name(parameters):
#     body of method
#
#
# method_name()===>invoking method
def print_hello():
    print("Hello Sneha")
    print("\n")

print_hello()


def print_hey(value):  # passing value while invoking method
    print("Hey")
    print(value)
    print("\n")


print_hey(5)  # value is passed


# PRINT "HELLO" 5 TIMES
def hello_method():
    for i in range(1, 5 + 1):
        print("Hello")
    print("\n")


hello_method()


# PRINTING SQUARE OF NUMBERS

def sqaure_no(n):
    for i in range(1, n + 1):
        # print(f"{i}*{i}={i*i}")
        # print("{0}*{0}={1}".format(i, i*i))  # WE CAN USE ANYONE TO PRINT
        print(i * i)
    print("\n")


sqaure_no(5)


# PRINT MULTIPLICATION TABLE FOR n

def tables(n):
    for i in range(1, 11):
        print(f"{n}*{i}={n * i}")
    print("\n")


tables(4)

# WORKING OF Indentation
def method_of_understand_indentation():
    for i in range(1, 11):
        print(i)  # THIS IS PRESENT INSIDE THE FOR LOOP
    print("Sneha")   # THIS IS PRESENT INSIDE METHOD BUT NOT IN FOR LOOP SO IT WILL PRINT ONLY ONCE
    print("\n")


method_of_understand_indentation()