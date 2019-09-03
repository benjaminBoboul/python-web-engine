from page import Page


class Engine(object):
    def __init__(self):
        self._index = {}
        self._search_counter = 0

    def index(self, page: Page):
        for word in page.words:
            if word in self._index:
                self._index[word].add(page)
            else:
                self._index[word] = {page}

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
            return [x.url for x in res]

    def multiple_search(self, words, and_mode=True):
        results = set()
        for word in words:
            ask = self.single_search(word)
            if ask:
                for item in ask:
                    results.add(item)
        return results if and_mode else results
