#! python3
# phoneAndEmail.py - Finds phone numbers and email address on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code
    (\s|-|\.)?                          # separator
    (\d{3})                             # first 3 digits
    (\s|-|\.)                           # separator
    (\d{4})                             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
)''', re.VERBOSE)

# Create eail regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username           
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domail name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for gorups in phoneRegex.findall(text):
    phoneNum = '-'.join([gorups[1], gorups[3], gorups[5]])
    if gorups[8] != '':
        phoneNum += ' x' + gorups[8]
    matches.append(phoneNum)
for gorups in emailRegex.findall(text):
    matches.append(gorups[0])

# Copy results to the clipboard.
if len(matches) > 0 :
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipbard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')

