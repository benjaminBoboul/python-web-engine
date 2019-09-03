class Page(object):
    def __init__(self, url, description, dictionnaire):
        self.url = url
        self.description = description
        self.dictionnaire = dictionnaire # mots contenu dans la description
        pass

    def __repr__(self):
        return "Page({}, {}, {})".format(self.url, self.description, self.dictionnaire)