import web
from engine import Engine
from pprint import pprint as pp

if __name__ == '__main__':
    engine = Engine()
    for url in open("urls.txt").readlines():
        engine.index(web.search(url.strip()))
    print(engine.indexed_words())
    pp(engine.indexed_url())

    keyword = "guns"
    keywords = ["over"]

    pp(engine.single_search(keyword))
    pp(engine.multiple_search(keywords))
    pp(engine.multiple_search(keywords, False))
