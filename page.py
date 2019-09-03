import string


class Page(object):
    def __init__(self, url, description):
        self._url = url
        self._description = description
        self._words = []
        if len(self._description) != 0:
            self._extract_words()

    @property
    def url(self):
        return self._url

    @property
    def description(self):
        return self._description

    @property
    def words(self):
        return self._words

    def __repr__(self):
        return "url: {},\ndescription: {},\nkeywords: {}".format(self._url, self._description, self._words)

    def _extract_words(self):
        self._words = self._description
        for c in list(string.punctuation)+['…']: self._words.replace(c, '')
        self._words = [x.lower() for x in self._description.split()]
