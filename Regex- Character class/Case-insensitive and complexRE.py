import re

# case Insensitive: we can use re.IGNORECASE or re.I as a second parameter to re.compile()

robocop = re.compile(r'robocop', re.I)
m0 = robocop.findall('rObOcop roboCOP')
m1 = robocop.search('Robocop is part man, part machine,all cop')
print(m0)
print(m1.group())

# Substituting strings with sub() method
# if sub method is used instead of search then dont use group method to print direct you can print

namesRegex = re.compile(r'Agent \w+')
m2 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob')
print(m2)

agentNamesRegex = re.compile(r'Agent (\w)\w+')
m3= agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double Agent.')
print(m3)


# The verbose mode can be enables by passing the variable re.VERBOSE as the second argument to re.compile()
