import web
from engine import Engine
from pprint import pprint as pp

if __name__ == '__main__':
    engine = Engine()
    for url in open("urls.txt").readlines():
        engine.index(web.search(url.strip()))

    page = web.search("https://www.lemonde.fr/")
    engine.index(page)
    print(engine.indexed_words())
    pp(engine.indexed_url())

    keyword = "guns"
    keywords = ["japanese"]

    pp(engine.single_search(keyword))
    pp(engine.multiple_search(keywords))
    pp(engine.multiple_search(keywords, False))

    pp(engine.single_search("international"))
    engine.deindex(page)
    pp(engine.single_search("international"))

    pp(engine.single_search("japanese"))
    pp(engine.single_search("business"))
