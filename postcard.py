from string import whitespace

# A string containing all characters that are considered whitespace. 
# On most systems this includes the characters space, tab, linefeed, 
# return, formfeed, and vertical tab.

codeFile = open('bs_js.js', 'r')
codeString = codeFile.read()
codeString = codeString.translate(dict.fromkeys(map(ord, whitespace), ''))

print(codeString)
