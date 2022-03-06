import re
# r'' is raw string to ignore escaping character nature
# \d in regex to find the digit character
phonenumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumberRegex.search('My number is 452-452-4424')
print('Phone number found:', mo.group())

# Steps invloved here is
# 1] import regex module with import re
# 2] create regex object with re.compile
# 3] pass the String which you want to search using regex object search()
# 4] call the match object's group() method to return a String of the actual matched text