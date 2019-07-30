import urllib.request
from bs4 import BeautifulSoup

class ParseWeb():
    def __init__(self,link):
        self.link = link
        self.title = None
        self.text = None
        self.thepage = urllib.request.urlopen(self.link)
        self.soup = BeautifulSoup(self.thepage,"html.parser")

    def parse_jutarnji(self):
        mydivs = self.soup.findAll("section", {"class": "ci_body"})
        text = mydivs[0].div.text
        title = self.soup.select('title')

        self.text = text
        self.title = title[0].text
        return

    def parse_vecernji(self):
        article_text = ""
        mydivs = self.soup.find("div", {"class": "article__body--main_content"}).findAll('p')
        for element in mydivs:
            article_text += ''.join(element.findAll(text=True))
        title = self.soup.select('title')

        self.title = title[0].text
        self.text = article_text
        return

    def parse_index(self):
        return
