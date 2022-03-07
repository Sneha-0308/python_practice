spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[0])
print('I hate ' + spam[0])

# print(spam[1.0]) ==>Wrong
print(spam[int(1.0)])  # ==>> correct

spam = [['cat', 'bat'], ['rat', 'elephant']]
print('I like '+spam[1][1])

# Negative indexes
#        -4     -3     -2        -1
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])

# slicing which creates new list from existing list
# in slicing it includes first range of value and excludes last range value
print(spam[1:4])
print(spam[:4])  # default value is zero
print(spam[0:])  # default value is length of spam
# print(len(spam))
print(spam[:])

# change the value in the list using indexes
spam[0] = 'dog'
print(spam)
spam[-2] = 12345
print(spam)  # Single list can store multiple datatype

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = ['a', 'b', 'c', 'd']
# concatenation
print(a+b)  # [1, 2, 3, 4, 10, 20, 30, 40]
print(a+c)   # [1, 2, 3, 4, 'a', 'b', 'c', 'd']

#  replication
print(a*3)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
del a[1]
print(a)

print(spam)
for i in range(len(spam)):
    print(spam[i])

for i in spam:
    print(i)

# in operator
result = 1 in [1, 2, 3, 4]
print(result)  #True
result = 100 in [1, 2, 3, 4]
print(result)  #False

# not in operator
result = 1 not in [1, 2, 3, 4]
print(result)


# Multiple assignment trick
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat  # same as a, b, c, = 1, 2, 3
# enumerate function give the two values of list the one is index and item under that index
for index, item in enumerate(cat):
    print('index '+ str(index)+' contains '+ item)


import random
print(random.choice(cat))
# print(random.shuffle(b))

test = ['cat', 'rat', 'bat', 'elephant']
print(test.index('rat'))
test.append('dog')
print(test)

test.insert(5,'dog')
print(test)

test.remove('dog')
print(test)

sorting = [1, 6, 4, 9,3 ,4,]
sorting.sort()
print(sorting)
sorting.sort(reverse = True)
print(sorting)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
# ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
spam.sort()
print(spam)
spam.sort(key = str.lower)
print(spam)
# ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']

spam.reverse()
print(spam)
# ['cats', 'Carol', 'Bob', 'badgers', 'ants', 'Alice']

spam = (1, 2, 3, 4)
print(spam)
test = ('abc')
print(type(test)) # <class 'str'>
test = ('abc',)
print(type(test)) # <class 'tuple'>


print(tuple(['cat','dog',5]))
print(list(('cat','dog',5)))