import urllib.request
from bs4 import BeautifulSoup

class ParseWeb():
    def __init__(self,link):
        self.link = link
        self.title = None
        self.text = None

    def parse_jutarnji(self):
        thepage = urllib.request.urlopen(self.link)
        soup = BeautifulSoup(thepage,"html.parser")
        mydivs = soup.findAll("section", {"class": "ci_body"})
        text = mydivs[0].div.text
        title = soup.select('title')
        self.text = text
        self.title = title[0].text
        return

    def parse_vecernji(selfs):
        return

    def parse_index(self):
        return
