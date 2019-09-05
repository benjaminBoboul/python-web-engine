import web
from termcolor import colored

from engine import Engine
from pprint import pprint as pp


if __name__ == '__main__':
    engine = Engine()
    for url in open("urls.txt").readlines():
        engine.index(web.search(url.strip()))

    page = web.search("https://www.lemonde.fr/")
    engine.index(page)

    pg = lambda x: print(colored(x.upper(), "green"))

    pg("Indexed words :")
    print(engine.indexed_words())

    pg("Indexed urls :")
    pp(engine.indexed_url())

    keyword = "guns"
    keywords = ["japanese"]

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

    pg("Result for tests for ranking")
    pp(engine.single_search("japanese"))
    pp(engine.single_search("business"))
