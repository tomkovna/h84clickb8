import urllib.request
from bs4 import BeautifulSoup

"""Class used for getting article content (title and text) from online link
 Class attributes are:
   link : online link, ex. https://www.gloria.hr/fokus/zvjezdane-staze/na-spici-smo-uhvatilii-poznatu-mamu-i-njezine-dvije-kceri-na-njihov-plan-bi-svatko-pristao/9180275/
   title: article title, ex. This article is shitty
   text: article body, main text
   thepage: irllib class casher from link
   soup: beautifulsoup class that parses html from thepage"""

class ParseWeb():
    def __init__(self,link):
        self.link = link
        self.title = None
        self.text = None
        self.thepage = urllib.request.urlopen(self.link)
        self.soup = BeautifulSoup(self.thepage,"html.parser")

    #TODO: svaka je metoda ista jedina je razlika sto je u jutarnjem glavni dio texta u sectionu, a
    # u vecernjem i indexu je u divu, te je naziv classa drugaciji, mozda se moze pametnije napravit :-)

    def parse_jutarnji(self):
        article_text = ""
        mydivs = self.soup.find("section", {"class": "ci_body"}).findAll('p')
        for element in mydivs:
            article_text += ''.join(element.findAll(text=True))
        title = self.soup.select('title')

        self.title = title[0].text
        self.text = article_text
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
        article_text = ""
        mydivs = self.soup.find("div", {"class": "text-holder"}).findAll('p')
        for element in mydivs:
            article_text += ''.join(element.findAll(text=True))
        title = self.soup.select('title')

        self.title = title[0].text
        self.text = article_text
        return

    def parse_story(self):
        article_text = ""
        mydivs = self.soup.find("div", {"class": "article__content"}).findAll('p')
        for element in mydivs:
            article_text += ''.join(element.findAll(text=True))
        title = self.soup.select('title')

        self.title = title[0].text
        self.text = article_text
        return

    def parse_tportal(self):
        article_text = ""
        mydivs = self.soup.find("section", {"class": "articleComponents"}).findAll('p')
        for element in mydivs:
            article_text += ''.join(element.findAll(text=True))
        title = self.soup.select('title')

        self.title = title[0].text
        self.text = article_text
        return

    def parse_24sata(self):
        article_text = ""
        mydivs = self.soup.find("div", {"class": "article__text"}).findAll('p')
        for element in mydivs:
            article_text += ''.join(element.findAll(text=True))
        title = self.soup.select('title')

        self.title = title[0].text
        self.text = article_text
        return
