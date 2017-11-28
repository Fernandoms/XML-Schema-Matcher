import xml.sax
import similarityFunctions as sF


class ContentHandler(xml.sax.ContentHandler):
    elements = []

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        if not ContentHandler.elements.__contains__(name):
            ContentHandler.elements.append(name)

    @staticmethod
    def getElementWords(self):
        return ContentHandler.elements


def demo():
    source = open("reed1.xml")
    ch = ContentHandler()
    xml.sax.parse(source, ch)
    elements1 = ContentHandler.getElementWords(ch)

    source2 = open("reed1.xml")
    ch2 = ContentHandler()
    xml.sax.parse(source2, ch2)
    elements2 = ContentHandler.getElementWords(ch2)

    for i in elements1:
        best_value = 0
        best_match = ""
        for j in elements2:
            sim = sF.JaroWinkler.similarity(i, j)
            if sim > best_value:
                best_value = sim
                best_match = j
        print(i + " - " + best_match + " " + str(best_value))


if __name__ == "__main__":
    demo()
