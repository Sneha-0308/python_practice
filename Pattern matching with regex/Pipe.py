# MATCHING MULTIPLE GROUPS WITH THE PIPE
# this file is related to match one from many patterns ie 2 either this or that ->>>any one from 2
# Pipe is used to match one of many expression

# NOTE: IF YOU WANT TO PASS THE MO.GROUP(1) OR ANY INDEX THEN IN RAW STRING THE REGEX OR STRING MUST ENCLOSED WITHIN
# PARENTHESIS
import re
hereRegex = re.compile(r'Batman|Tina Fey')
# hereRegex = re.compile(r'(Batman)|(Tina Fey)') ===>>>print(mo1.group(1))

mo1 = hereRegex.search('Batman and Tina Fey')
mo2 = hereRegex.search('Tina Fey and Batman')
print(mo1.group())
print(mo2.group())