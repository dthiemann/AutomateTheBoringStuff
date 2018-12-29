import webbrowser, sys, pyperclip, requests, bs4, os

# Web Scrapping - Automate The Boring Stuff - Chapter 11


def main():
    print("Main script")
    # openBrowserToUrl("https://www.google.com")
    # googleMapsAddress()
    # getRequest("https://automatetheboringstuff.com/files/rj.txt")
    # handleFailedRequest("http://inventwithpython.com/page_that_does_not_exist")
    getXkcdComics()


def openBrowserToUrl(url):
    webbrowser.open(url)


def googleMapsAddress():
    if (len(sys.argv)) > 1:
        # Get address from command line
        address = " ".join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open("https://www.google.com/maps/place/" + address)


# Handling requests
def getRequest(url):
    res = requests.get(url)
    print(type(res), res)
    print(len(res.text))
    print(res.text[:100])


def handleFailedRequest(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as ex:
        print("there was a problem: %s" % (ex))


def getXkcdComics():
    url = "http://xkcd.com"  # starting URL
    os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd`
    i = 0
    while not url.endswith("#") and i < 20:

        # Download the page
        i += 1

        print("Downloading page %s..." % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # TODO: Find the URL of the comic image

        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image")
        else:
            try:
                comicUrl = "http:" + comicElem[0].get("src")

                # Download the image
                print("Download image %s..." % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                # skip this comic
                prevLink = soup.select('a[rel="prev"]')[0]
                url = "http://xkcd.com" + prevLink.get("href")
                continue

            # TODO: Save the image to ./xkcd

            iamgeFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
            for chunk in res.iter_content(100000):
                iamgeFile.write(chunk)
            iamgeFile.close()

        # TODO: Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com" + prevLink.get("href")

    print("Done.")


main()
