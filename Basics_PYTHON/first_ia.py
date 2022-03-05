# i =0
# while(i<=5):
#     print(i)
#     if(i==3):
#         break
#     i+=1

# i = 0
# while(i<6):
#     i+=1
#     if(i==3):
#         continue
#     print(i)

# sum = 0
# for i in range(10):
#     sum +=i
#     print(sum)

# for i in range(5):
#     print(i)
#
# def greet(name):
#     print("hey "+name)
# greet("sneha")

# def greet(*name):
#     print(name[1])
# greet('sneha','ruby')
# def greet(name='sneha'):
#     print("hey ",name)
# greet()

# a=4
# b=5
# c=int(a)+int(b)
# print("values are {},{},{}".format(a,b,a))
#
# def fun():
#     str = "computer Science"
#     x = len(str)
#     return str, x
# # str, x = fun()
# # print(str)
# # print(x)
# fun()

# def outer(x):
#     return x * 10
# def my_func():
#         return outer
#  # storing the function in res
# res = my_func()
# print("\nThe result is:", res(10))
#
#
# num = int(input("enter number"))
# count = 0
# for i in range(2, num//2+1):
#     if(num%i==0):
#         count+=1
#         break
# if(count==0 and num!=1):
#     print("it is prime number")
# else:
#     print("it is not a prime number")

# num = [1, 2, 3, 4, 5]
# print(max(num))

# size=int(input("enter size of list"))
# num=[]
# for i in range(1,size+1):
#     val=int(input("enter value"))
#     num.append(val)
# print(num)
# print("largest number is ", max(num))
# print("smallest number is ",min(num))

# def test(a,b,c):
#     print(b)
# test(c=1,a=2,b=4)

# def greeting():
#     x = "sneha"
#     y = 'ruby'
#     return x, y
#
#
# x, y = greeting()
# print(x)
# print(y)
#
# def greeting(x):
#     return 1*x
#
#
# def test():
#     return greeting
#
# res=test()
# print(res(100))

def div(test):
    try:
        return 10/test
    except ZeroDivisionError:
        return 'invalid argument'


print(div(3))
