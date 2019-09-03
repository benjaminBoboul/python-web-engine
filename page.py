import string


class Page(object):
    def __init__(self, url, description):
        self._url = url
        self._description = description
        self._words = None
        if len(self._description) != 0:
            self._extract_words()

    def __repr__(self):
        return "Page(url:{}, description:{}..., keywords:{})".format(self._url, self._description[:50], self._words)

    def _extract_words(self):
        punctuation = list(string.punctuation)
        punctuation.append('…')
        self._words = self._description.lower()
        self._words = [x for x in self._words.split()]
