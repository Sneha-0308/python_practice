import re

# By using [] we can form our own character class
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo1)

# caret (^) is acts like negation
consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo2 = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo2)


