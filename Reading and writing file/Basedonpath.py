from pathlib import Path
import os

print(Path('spam', 'bacon', 'eggs'))

myFiles = ['abc.txt', 'xyz.py']
for fileName in myFiles:
    print(Path(r'c:vsdf\all', fileName))
    print(os.path.join(r'c:xyz/', fileName))

print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon', 'eggs'))
print(Path('spam') / Path('bacon/eggs'))

print(os.path.join('user', 'xyz', 'abc'))
'''we can use both method either Path() from pathlib or os.path.join from os module
    os.path.join() function if you pass it the string values of individual file and folder names in your path,
    os.path.join() will return a string with a file path using the correct path separator
'''

'''You can get the current working directory as a string value with the os.getcwd() function and change it with 
os.chdir() function '''
print(os.getcwd())
'''os.chdir('c:\windows\System32')
    print(os.getcwd)
    o/p::: c:\windows\System32 '''

# os.makedirs('mention path where you want to create directory by
# mentioning the dir name at the end of path')



# RELATIVE AND ABSOLUTE PATH
print(os.path.abspath('.'))
print(os.path.isabs('.'))
# os.path.relpath(path,start)
print(os.path.relpath('c://Windows', 'c://'))

'''os.path.dirname(path)->> it returns a String of everything that comes before the last slash in the path arguments 
    os.path.basename(path)->> it returns a string of everything that comes after the last slash in the path argument'''
path = 'C:\Windows\System32\calc.exe'
print(os.path.dirname(path))
# C:\Windows\System32
print(os.path.basename(path))
# calc.exe

'''we can use os.path.split(path) if you need path's dir name and base name together it gives the output in tuples'''
add = 'C:\Windows\System32\calc.exe'
print(os.path.split(add))

'''If you want return list of dir and file names then we use split() string method and split on the string in os.path.sep'''
print(add.split(os.path.sep))



# FINDING THE FILE SIZES AND FOLDER CONTENT
path = os.getcwd()
print(path)
print(os.path.getsize(path))

print(os.listdir(path))


'''TO FIND THE TOTAL SIZE OF THR FILES IN THIS DIRECTORY WE CAN USE OS.PATH.GETSIZE AND OS.LISTDIR'''
# totalsize = 0
# for filename in os.listdir(path):
#     totalsize += os.path.getsize(os.path.join('path address', filename))
# print(totalsize)



