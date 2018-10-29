class Document:

    def __init__(self, text: str, tag: str = '') -> None:
        self._text = text.strip()
        self._text_as_list = []
        self._tag = tag.strip()

    def getText(self) -> str:
        return self._text
