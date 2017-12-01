from lxml import etree

class XMLData(object):
    ''' Objeto para servir de elemento na árvore que representa o XSD'''

    def __init__(self, tag_name):
        self.tag_name = tag_name

    def add_occurs(self, max, min):
        self.max_occurs = max
        self.min_occurs = min

    def add_type(self, type):
        self.type = type

    def add_path(self, path):
        self.path = path

    def add_name(self, name):
        self.name = name


class Node(object):
    ''' Elemento estrutural da árvore '''

    def __init__(self, tree, root):
        self.children = []
        self.data = Node.set_data(tree, root)
        for child in root.getchildren():
            self.children.append(Node(tree, child))

    @staticmethod
    def set_data(tree, element):
        xmlData = XMLData(element.tag)
        xmlData.add_occurs(element.get('maxOccurs'), element.get('minOccurs'))
        xmlData.add_type(element.get('type'))
        xmlData.add_path(tree.getpath(element))
        xmlData.add_name(element.get('name'))
        return xmlData

    def print_tree(self, level=0):
        print ('\t' * level + repr(self.data.tag_name), " Args ", self.data.name, self.data.max_occurs, self.data.min_occurs, self.data.type, self.data.path,  sep=' - ')
        for child in self.children:
            child.print_tree(level + 1)


def demo():
    tree = etree.parse('/home/fernandoms/Desktop/NewXMLSchema.xsd')
    root = tree.getroot()
    structural_tree = Node(tree, root)
    structural_tree.print_tree()

if __name__ == '__main__':
    demo()
