import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex.search('Cell: 452-452-4444 Work: 452-452-3333 ')
# search object gives only one pattern search which comes first
print(mo1.group())
mo2 = phoneNumberRegex.findall('Cell: 452-452-4444 Work: 452-452-3333 ')
print(mo2)

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneRegex.findall('Cell: 452-452-4444 Work: 452-452-3333 ')
print(mo)
# findall() object gives list of  pattern
'''
-->> When called on a regex with no groups, the method findall() reurns
a list of Strings matches

-->> When called on a regex with groups, the method findall() reurns
a list of tuples of Strings matches'''