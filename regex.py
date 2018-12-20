# Regex - Automate the Boring Stuff

import pyperclip, re

# Phone Number
# 1. area code
# 2. separator
# 3. first 3 digits
# 4. last 4 digits
# 5. extension
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\d{4})
    (\s*{ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

# Email
# 1. First segemnt (before @ - alphanumeric uncluding underscore and dash)
# 2. @ symbole
# 3. domain name
# 4. dot-something
emailRegex = re.compile(r'''(
    ^[a-zA-Z0-9_-]+
    (@)
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Returns true if the password is strong, false if not
# At least 8 characters long
# Contains both upper and lower case
# Has at least 1 digit
def strongPassword(password):
    characterLengthRegex = re.compile(r'\S'{8,})
    upperLowerRegex = re.compile(r'[a-z]')
