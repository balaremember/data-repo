class Corpus:

    def __init__(self) -> None:
        self.__pathToFile = ''
        self.__documents = []

    def loadCorpusFromList(self, documents: list, tags: list = []) -> None:
        from LabWorks.algoritms.plsaLib.Document import Document
        for index in range(len(documents)):
            try:
                self.__documents.append(Document(documents[index], tags[index]))
            except IndexError:
                self.__documents.append(Document(documents[index], ''))

    def getDocuments(self) -> list:
        return self.__documents
