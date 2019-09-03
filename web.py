from urllib.parse import urlparse as up
import bs4
from requests import get
import string
from page import Page
from engine import Engine


def download(url: string):
    pu = up(url)
    page = get(pu.geturl()) if pu.scheme in ["http", "https"] and pu.netloc != '' else None
    content = page.content if page.status_code == 200 else None
    return pu.geturl(), page.status_code, content


def parseDescription(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    property_description = soup.find('meta', {'property': 'og:description'})
    return property_description.get('content').strip() if property_description else None


def search(url: string):
    socket, status, content = download(url)
    description = parseDescription(content) if content else None
    return Page(socket, description)


if __name__ == '__main__':
    engine = Engine()
    for line in open("urls.txt").readlines():
        page = search(up(line.strip()).geturl())
        print(page)
        if page.description:
            engine.index(page)

    print(engine.indexed_url())
    print(engine.indexed_words())
    print("Recherche get :\n", engine.single_search("get"))
    print("Recherche multiple sans corrélation :\n", engine.multiple_search(["intelligence", "behaviour"], False))
    print("Recherche multiple avec corrélation :\n", engine.multiple_search(["intelligence", "behaviour"]))

