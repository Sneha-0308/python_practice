import re

# caret symbol without [] this find match occur at the beginning
beginWithHello = re.compile(r'^Hello')
mo = beginWithHello.search('Hello world!')
print(mo is None)
m1 = beginWithHello.search('He said Hello.')
print(m1 is None)


# The r'\d$' RE String matches Strings that end with a numeric character from 0 to 9
endsWithNumber = re.compile(r'\d$')
m2 = endsWithNumber.search('Your number is 42')
m3 = endsWithNumber.search('Your number is forty two')
print(m2 is None)
print(m3 is None)


#  The r'^\d+$' Re string, matches strings that both begin and ends with one or more numeric characters.
wholeStringIsNum = re.compile(r'^\d+$')
m4 = wholeStringIsNum.search('1234567890')
print(m4 is None) #False
m5 = wholeStringIsNum.search('1234567890 xyz')
m6 = wholeStringIsNum.search('abcd 1234567890 xyz')
print(m5 is None)  #True
print(m6 is None)  #True





