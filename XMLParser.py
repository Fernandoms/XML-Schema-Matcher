import xml.sax
import similarityFunctions as sf

class ContentHandler(xml.sax.ContentHandler):
    elements = []
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        if not ContentHandler.elements.__contains__(name):
            ContentHandler.elements.append(name)

    def getElementWords(self):
        return (ContentHandler.elements)


def demo():
    source = open("reed1.xml")
    ch = ContentHandler()
    xml.sax.parse(source,ch)
    elements1 =ContentHandler.getElementWords(ch)


    source2 = open("reed1.xml")
    ch2 = ContentHandler()
    xml.sax.parse(source2,ch2)
    elements2 = ContentHandler.getElementWords(ch2)

    for i in elements1:
        bestValue = 0
        bestMatch = ""
        for j in elements2:
            sim = sf.JaroWinkler.similarity(i,j)
            if (sim > bestValue):
                bestValue = sim
                bestMatch = j
        print (i + " - " + bestMatch + " " +str(bestValue))

if __name__ == "__main__":
    demo()