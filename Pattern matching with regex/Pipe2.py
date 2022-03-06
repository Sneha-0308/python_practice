# this file is related to  one from several patters
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = batRegex.search('Batmobile lost a wheel')
mo2 = batRegex.search('Batbat')
print(mo1.group())
print(mo2.group())