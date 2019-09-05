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
        print("Recherche du terme : %s\n--------------------" % word)
        if word.lower() not in self._index:
            return []
        else:
            result = list(self._index.get(word.lower()))
            result.sort(key=lambda x: x.words[word], reverse=True)
            return [("occurrences : %s" % x.words[word], x) for x in result]

    def multiple_search(self, words, and_mode=True):
        res = {}
        for tag in words:
            res[tag] = self.single_search(tag)

        return res

        # results = set()
        # for word in words:
        #     ask = self.single_search(word)
        #     if ask:
        #         for item in ask:
        #             results.add(item)
        # return results if and_mode else results