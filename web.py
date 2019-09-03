from urllib.parse import urlparse as up
import bs4
from requests import get
import string
from page import Page

def download(url: string):
    pu = up(url)
    page = get(pu.geturl()) if pu.scheme in ["http", "https"] and pu.netloc != '' else None
    content = page.content if page.status_code == 200 else None
    return pu.geturl(), page.status_code, content


def parseDescription(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    property_description = soup.find('meta', {'property': 'og:description'})
    return property_description.get('content').strip() if property_description else None


def extractKeywords(sentence: string):
    if sentence is None:
        return None
    return sentence.translate(sentence.maketrans('', '', string.punctuation)).split(" ")


def search(url: string):
    socket, status, content = download(url)
    description = parseDescription(content) if content else None
    parsed_description = extractKeywords(description) if description else None
    page = Page(socket, description, parsed_description)
    print(page)


if __name__ == '__main__':
    for line in open("urls.txt").readlines():
        search(up(line.strip()).geturl())
