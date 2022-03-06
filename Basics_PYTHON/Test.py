# x, y, z = 'dog', 'cat', 'snake'
# print(x)
# print(y)
# print(z)
#
#
# x = y = z = 'camel'
# print(x)
# print(y)
# print(z)


# print('hello, world!')
# name = str(input('What is your name'))
# print('My name is ', name)


# name1 = 'sneha mathadawar'
# print(len(name1))
#
# a = ''
# print(len(a))


# print(True or False)
# print(not True)
#
# while(True):
#     name = str(input('Enter your name'))
#     if name == 'sneha':
#         break
#
# print('Thank you')

#
# while(True):
#     username=str(input('enter username'))
#     if(username != 'sneha'):
#         continue
#     password = str(input('sneha enter your password:'))
#     if(password == 'sneha'):
#         break
# print('Thankyou')

# for i in range(2,5):
#     print('hey')

# import sys
# while(True):
#     text = str(input('Type exit to exit'))
#     if(text == 'exit'):
#         # sys.exit()
#     print('thank you')

#
# def myname():
#     print('my name is sneha')
# myname()
#
# def myname(name):
#     print('my name is',name)
# myname('sneha')

# spam = print('sdugy')
# print(None is spam)

# print('hey', end='')
# print('hey')
#
# print('cat', 'dogs', 'mice')
# print('cat', 'dogs', 'mice',sep=',')

# def fun():
#     print(egg)
# egg=2
# fun()
# print(egg)

# def spam():
#     global eggs
#     eggs='spam'
#     eggs='cdf'
# eggs = 'global'
# # print(eggs)
# spam()
# print(eggs)

def divide(num):
    try:
        print(10/num)
    except ZeroDivisionError:
        print("ERROR")

divide(1)