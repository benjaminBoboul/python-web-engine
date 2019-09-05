from page import Page


class Engine(object):
    def __init__(self):
        self._index = {}

    def index(self, page: Page):
        for tag in page.words:
            if tag in self._index:
                self._index[tag].add(page)
            else:
                self._index[tag] = {page}

    def deindex(self, page: Page):
        for tag in page.words:
            if tag in self._index:
                if page in self._index[tag]:
                    self._index[tag].remove(page)
                    if self._index[tag] is 0:
                        self._index.pop(tag)

    def indexed_url(self):
        urls = set()
        for page_set in self._index.values():
            if page_set:
                page_url = [x.url for x in page_set]
                urls = urls.union(page_url)
        return tuple(urls)

    def indexed_words(self):
        return tuple(x for x in self._index.keys())

    def single_search(self, word):
        if word.lower() not in self._index:
            return []
        else:
            result = self._index.get(word.lower())
            print("Found %i results :" % len(result))
            return tuple(sorted(result, key=lambda k: k.words[word], reverse=True))

    def multiple_search(self, words, and_mode=True):
        urls = set()
        if len(words) == 0:
            return []
        if not and_mode:
            for tag in words:
                urls.update(self.single_search(tag))
        else:
            urls.update(self.single_search(words[0]))
            for tag in words[1:]:
                urls = urls.union(self.single_search(tag))
        return tuple(urls)
