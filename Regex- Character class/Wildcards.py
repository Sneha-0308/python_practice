
# Wildcards character
# The . character in Re is called wild card and will match any character except for a new line.


# .  character will much only one character
import re
atRegex = re.compile(r'.at')
m0 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(m0)

# .* to stand in for that anything
nameRegex = re.compile(r'.*')
m1 = nameRegex.search('sneha mathadawar fhe647/ %**')
print(m1)
print(m1.group());

fullName = re.compile(r'first name:.* last name: .*')
m2 = fullName.search('first name: abc last name: xyz')
print(m2 .group())


# Greedy and NonGeerdy

nongreedyRegex = re.compile(r'<.*?>')
greedyRegex = re.compile(r'<.*>')
m3 = nongreedyRegex.search('<To serve man> for dinner.>')
m4 = greedyRegex.search('<To serve man> for dinner.>')
print(m3.group())
print(m4.group())


# Matching Newlines with the Dot character
# Dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile() you can make the
# dot character match all character including the new line chacters
noNewLineRegex = re.compile(r'.*')
m5 = noNewLineRegex.search('Serve the public trust.\nProtect the innocents.\nUphold the law.')
print(m5.group())  #Output: Serve the public trust.
newLineRegex = re.compile(r'.*',re.DOTALL)
m6 = newLineRegex.search('Serve the public trust.\nProtect the innocents.\nUphold the law.')
print(m6.group())

''' OUTPUT:
Serve the public trust.
Protect the innocents.
Uphold the law.
'''


