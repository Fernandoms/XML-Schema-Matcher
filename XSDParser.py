from lxml import etree

class XMLData(object):
    """ Objeto para servir de elemento na arvore que representa o XSD """
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.max_occurs = 0  #escolher default
        self.min_occurs = 0  #escolher default
        self.type = ''
        self.name = ''
        self.path = ''


class Node(object):
    """ Elemento estrutural da arvore """

    def __init__(self, tree, root, father = None):
        self.children = []
        self.father = father
        self.data = Node.set_data(tree, root)
        for child in root.getchildren():
            self.children.append(Node(tree, child, root))

    @staticmethod
    def set_data(tree, element):
        xmlData = XMLData(element.tag)
        xmlData.max_occurs = element.get('maxOccurs')
        xmlData.min_occurs = element.get('minOccurs')
        xmlData.type = element.get('type')
        xmlData.path = tree.getpath(element)
        xmlData.name = element.get('name')
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
