from urllib.parse import urlparse as up
import bs4
import requests as r
import string


def download(url: string):
    parsed_url = up(url)
    if parsed_url.scheme in ["http", "https"] and parsed_url.netloc != '':
        page = r.get(parsed_url.geturl())
        if page.status_code == 200:
            return parsed_url.geturl(), page.status_code, page.content


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
    description = parseDescription(content)
    parsed_description = extractKeywords(description)
    print(socket, status, description, parsed_description)


if __name__ == '__main__':
    search("https://korben.info/")
    search("https://www.google.fr/")
    search("http://www.lemonde.fr/")
    search("https://www.lemonde.fr/societe/live/2019/09/03/que-faut-il-attendre-du-grenelle-des-violences-conjugales-posez-vos-questions_5505754_3224.html")
    search("http://imt-lille-douai.fr/")
