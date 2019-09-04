from page import Page
import string

class Engine(object):
    def __init__(self):
        self._index = {}
        self._search_counter = 0

    def _extract_occurency(self, page: Page, keyword: string):
        pass

    def index(self, page: Page):
        for tag in page.words:
            if tag in self._index:
                self._index[tag].add(page)
            else:
                self._index[tag] = {page}

    def deindex(self, page: Page):
        for tag in page.words:
            if tag in self._index:
                if len(self._index[tag]) > 1 and page in self._index[tag]:
                    self._index[tag].remove(page)
                elif len(self._index[tag]) == 1 and page is self._index[tag]:
                    del(self._index[tag])

    def indexed_url(self):
        urls = set()
        for page_set in self._index.values():
            if page_set:
                page_url = [x.url for x in page_set]
                urls = urls.union(page_url)
        return urls

    def indexed_words(self):
        return {x for x in self._index.keys()}

    def single_search(self, word):
        res = self._index.get(word.lower())
        if res:
            return [x for x in res]

    def multiple_search(self, words, and_mode=True):
        results = set()
        for word in words:
            ask = self.single_search(word)
            if ask:
                for item in ask:
                    results.add(item)
        return results if and_mode else results
