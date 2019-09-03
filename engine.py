class Engine(object):
    def __init__(self):
        self._index = {}
        self._search_count = 0

    def index(self, page):
        for words in page.words:
            if words in self._index:
                self._index[words] = self._index[words].union({page})
            else:
                self._index[words] = {page}

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

    def multiple_search(self, words, and_mode=True): # TODO: Refactor
        result, urls = set(), [self.single_search(word) for word in words]
        return list(result & set(urls)) if and_mode else list(result + set(urls))
