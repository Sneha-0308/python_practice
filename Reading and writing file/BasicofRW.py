'''THERE ARE 3 STEPS TO READING OR WRITING FILES IN PYTHON
    1]call the open() function to return a file object.
    2]call the read() or write() method on the FIle object
    3]Close the  file by calling te close() method on file object'''

f0 = open('test.txt')  # here f0 is file object which is holding test.txt file
print(f0.readlines())
f0.close()
# it will print content in list format each line are separated by ',' if we dont have content it gives the empty list []


f1 = open('test.txt', 'w') # write mode overwrite the existing file and start from scratch
f1.write('Hello World!\n')
f1.close()

f1 = open('test.txt', 'a')  # Append mode will append text to the end of the existing file
f1.write('Bacon is not vegetable.')
f1.close()

f1 = open('test.txt')
content = f1.read()
f1.close()
print(content)  # it will display the content not in the list format