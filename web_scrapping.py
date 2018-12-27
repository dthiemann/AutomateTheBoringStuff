import webbrowser, sys, pyperclip

# Web Scrapping - Automate The Boring Stuff - Chapter 11


def main():
    print("Main script")
    # openBrowserToUrl("https://www.google.com")
    # googleMapsAddress()


def openBrowserToUrl(url):
    webbrowser.open(url)


def googleMapsAddress():
    if (len(sys.argv)) > 1:
        # Get address from command line
        address = " ".join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open("https://www.google.com/maps/place/" + address)

