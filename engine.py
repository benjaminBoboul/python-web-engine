class Engine(object):
    def __init__(self):
        self._index = {} #dict()
        self._search_count = 0

    def index(self, page):
        for words in page.words:
            if words not in self._index:
                self._index[words] = {page}
            else:
                self._index[words] = self._index[words].add(page)

    def indexed_url(self):
        return self._index.values()

    def indexed_words(self):
        return self._index.keys()

    def single_search(self, word):
        return self._index[word.lower()] or None

    def multiple_search(self, words, and_mode=True):
        if not and_mode:
            return [self.single_search(word) for word in words]
