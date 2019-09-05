from page import Page


class Engine(object):
    def __init__(self):
        self._index = {}
        self._search_counter = 0

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
                page_url = [x for x in page_set]
                urls = urls.union(page_url)
        return urls

    def indexed_words(self):
        return {x for x in self._index.keys()}

    def single_search(self, word):
        if word.lower() not in self._index:
            return []
        else:
            result = list(self._index.get(word.lower()))
            result.sort(key=lambda x: x.words[word], reverse=True)
            return [("occurrences : %s" % x.words[word], x) for x in result]

    def multiple_search(self, words, and_mode=True):
        self._search_counter += 1
        urls = set()
        if len(words) == 0:
            return []
        if not and_mode:
            for tag in words:
                urls.update(self.single_search(tag))
        else:
            tmp = set(self.indexed_url())
            for tag in words:
                tmp = tmp.intersection(self.single_search(tag))
            urls = tmp
        return list(urls)
