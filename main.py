import web
from termcolor import colored

from engine import Engine
from pprint import pprint as pp


if __name__ == '__main__':
    engine = Engine()
    pg = lambda x: print(colored(x.upper(), "green"))
    for url in open("urls.txt").readlines():
        page = web.search(url.strip())
        engine.index(page)
        pg("print page :")
        print(page)

    page = web.search("https://www.lemonde.fr/")
    engine.index(page)

    pg("Indexed words :")
    print(engine.indexed_words())

    pg("Indexed urls :")
    pp(engine.indexed_url())

    keyword = "guns"
    keywords = ["japanese", "people"]

    pg("Results for %s"% keyword)
    pp(engine.single_search(keyword))
    pg("Results for %s"% keywords)
    pp(engine.multiple_search(keywords))
    pg("Results for %s without and_Mode"%keywords)
    pp(engine.multiple_search(keywords, False))

    pg("Result for international")
    pp(engine.single_search("international"))
    pg("Deindexing entry")
    engine.deindex(page)
    pg("Result for international")
    pp(engine.single_search("international"))

    pg("Result for japanese")
    pp(engine.single_search("japanese"))
    pg("Result for business")
    pp(engine.single_search("business"))
