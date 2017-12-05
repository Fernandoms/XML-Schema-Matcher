from lxml import etree
import re
import copy


class XMLData(object):
    """ Objeto para servir de elemento na arvore que representa o XSD """

    def __init__(self, tag_name):
        self.tag_name = re.sub('({)(.*)(})', '', tag_name)
        self.max_occurs = 0  # escolher default
        self.min_occurs = 0  # escolher default
        self.type = ''
        self.name = ''
        self.path = ''
        self.value = ''

    def print_return(self):
        printable = ''
        if self.name is not None: printable += 'Name:' + self.name + ' - '
        if self.value is not None: printable += 'Value:' + self.value + ' - '
        if self.max_occurs is not None: printable += 'maxOccurs:' + str(self.max_occurs) + ' - '
        if self.min_occurs is not None: printable += 'minOccurs: ' + str(self.min_occurs) + ' - '
        if self.type is not None: printable += 'type: ' + self.type + ' - '
        if self.path is not None: printable += 'path' + self.path
        return printable


class Node(object):
    """ Elemento estrutural da arvore """

    def __init__(self, tree, root, anc=None, insert_children=True):
        self.children = []
        self.ancestor = anc
        self.data = Node.set_data(tree, root)
        if insert_children:
            for child in root.getchildren():
                self.insert_children(tree, child)

    def __str__(self):
        return  self.data.tag_name

    def insert_children(self, tree, child, insert_children=True):
        self.children.append(Node(tree, child, self, insert_children))

    @staticmethod
    def set_data(tree, element):
        if element is not None:
            xmlData = XMLData(element.tag)
            xmlData.max_occurs = element.get('maxOccurs')
            xmlData.min_occurs = element.get('minOccurs')
            xmlData.type = element.get('type')
            xmlData.path = tree.getpath(element)
            xmlData.name = element.get('name')
            xmlData.value = element.get('value')
            return xmlData
        else:
            return None

    def print_tree(self, level=0):
        print('\t' * level + str(self), " Args: ", self.data.print_return(), self.ancestor)
        for child in self.children:
            child.print_tree(level + 1)

    def print_tree_clean(self, root, level=0):
        for child in self.children:
            if child.data.tag_name in ('element', 'attribute'):
                print('\t' * level + child.data.tag_name, " Args: ", child.data.print_return())
            if child.data.type is not None and child.data.type[:3] != 'xsd':
                node = root.find_node_by_name(child.data.type)
                node.print_tree_clean(root, level + 1)
            else:
                child.print_tree_clean(root, level)

    def has_children(self):
        return self.children is not None

    def get_root(self):
        return self.ancestor.get_root() if self.ancestor is not None else self

    def find_node_by_name(self, name):
        if self.data.name == name:
            return self
        elif self.has_children():
            for child in self.children:
                if child.find_node_by_name(name) is not None: return child.find_node_by_name(name)
        else:
            return None

    @staticmethod
    def move_child(child, new_ancestor):
        child.ancestor.children.remove(child)
        child.ancestor = new_ancestor
        new_ancestor.children.append(child)

    def move_types(self):
        if self.data.type is not None and self.data.type[:3] != 'xsd':
            root = self.get_root()
            Node.move_child(root.find_node_by_name(self.data.type), self)

    def iterate(self):
        self.move_types()
        for child in self.children:
            child.iterate()


def demo():
    tree = etree.parse('/home/fernandoms/Desktop/NewXMLSchema.xsd')
    root = tree.getroot()
    structural_tree = Node(tree, root)
    structural_tree.iterate()
    structural_tree.print_tree()

if __name__ == '__main__':
    demo()
