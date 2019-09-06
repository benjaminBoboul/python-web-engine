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
            result = []
        else:
            result = sorted(self._index.get(word.lower()), key=lambda k: k.words[word], reverse=True)
        print("Found {} results for {}.".format(len(result), word.lower()))
        return tuple(result)

    def multiple_search(self, tags, and_mode=True):
        result, saved_tags = set(), set()
        if tags:
            result, saved_tags = result | set(self.single_search(tags[0])), saved_tags.union({tags[0]})
            for tag in tags[1:]:
                urls = self.single_search(tag)
                result, saved_tags = result.intersection(urls) if and_mode else result.union(urls), saved_tags.union({tag})
        return tuple(sorted(result, key=lambda x: saved_tags, reverse=True))
