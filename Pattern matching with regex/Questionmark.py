# import re
#
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The adventures of Batman')
# print(mo1.group())
# mo2 = batRegex.search('The adventures of Batwoman')
# print(mo2.group())

# Question mark-->The regex will match text that has 0 or 1 instance of wo in it



# ANOTHER PROGRAM FOR EXAMPLE

import re
phoneNumberRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex.search('My number is 452-452-4444')
mo2 = phoneNumberRegex.search('My number is 452-4444')
print(mo1.group())

print(mo2.group())



