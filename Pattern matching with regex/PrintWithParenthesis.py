import re

# \( \) by using escaping character with back slash '\' it will remove the actual meaning of () and prints with ()
phoneNumberRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My phone number is (452)-452-4444')
print(mo.group(1))
print(mo.group(2))