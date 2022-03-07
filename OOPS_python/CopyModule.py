import copy
'''
In deep copy any changes made to a copy of object do not reflect in the original object.
'''
print('Deep copy')
l1 = [[1, 2], [3, 4]]
print(l1)
cp = copy.deepcopy(l1)
print(cp)
cp[0][0]=45
print(cp)
print(l1)


'''In case of shallow copy constructing a new collection objects and then populating it with references to the child 
objects found in the original '''
print('Shallow copy')
l2 = [[1, 2], [3, 4]]
print(l2)
sh = copy.copy(l2)
print(sh)
sh[0][0]=45
print(sh)
print(l2)

#
# Deep copy
# [[1, 2], [3, 4]]
# [[1, 2], [3, 4]]
# [[45, 2], [3, 4]]
# [[1, 2], [3, 4]]
# Shallow copy
# [[1, 2], [3, 4]]
# [[1, 2], [3, 4]]
# [[45, 2], [3, 4]]
# [[45, 2], [3, 4]]