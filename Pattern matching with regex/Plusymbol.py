import re
batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batman')
# above line of code gives error because it has o occurrence of wo at least one wo must be present
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowoman')
# print(mo1.group())
print(mo2.group())
print(mo3.group())

# Plus is used to find one or more occurrences
