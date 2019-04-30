#! python3
# madlibs.py - Change text in text file to users' entered text in long sentence.

import re, os

madlibs = open("C:\\Users\\k2web\\Desktop\\python\\automation book\\madlibs.txt")
changeTexts = madlibs.read()
madlibs.close()

print(changeTexts)

change_regex = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')
matches = change_regex.findall(changeTexts)

for found in matches :
    sub = input('Enter a ' + found + ' : ')
    changeTexts = changeTexts.replace(found, sub, 1)

print(changeTexts)

changeMadlibs = open(os.getcwd()+os.path.sep+'new madlibs.txt', 'w')
changeMadlibs.write(changeTexts)
changeMadlibs.close()