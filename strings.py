#! python3

# Automate the boring stuff
# String - https://automatetheboringstuff.com/chapter6/

import sys,pyperclip

# Project 1 - Password Manager
def passwordManager():
    PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
                'luggage': '12345'}

    if len(sys.argv) < 2:
        print('Usage: python strings.py [account] - copy account password')
        sys.exit()

    account = sys.argv[1]

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copies to clipboard')
    else:
        print('There is no account named ' + account)

def bulletPointAdder():
    inputStrings = pyperclip.paste()
    if inputStrings == None or inputStrings = "":
        print("No strings in clipboard. Exiting program")
        return
    
    ubStrings = inputStrings.split('\n')
    for i in range(len(ubStrings)):
        ubStrings[i] = " * " + ubStrings[i]

    bStrings = '\n'.join(ubStrings)
    pyperclip.copy(bStrings)