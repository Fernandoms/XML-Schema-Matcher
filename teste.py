from lxml import etree
import xmlschema

class XMLData(object):
    def __init__(self, tag_name, path, min_occurs=1, max_occurs=1, type=None, ):
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self.tag_name = tag_name
        self.type = type
        self.path = path


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def print_tree(self, level=0):
        print ('\t' * level + repr(self.data.tag_name))
        for child in self.children:
            child.print_tree(level + 1)


tree = etree.parse('/home/fernandoms/Desktop/NewXMLSchema.xsd')
schema = xmlschema.XMLSchema('/home/fernandoms/Desktop/NewXMLSchema.xsd')


root = tree.getroot()

for el in tree.iter():
    print(el.tag)




'''root = tree.getroot()
root_schema = schema.find(tree.getpath(root))
print(root_schema)
print(tree.getpath(root))
root_info = XMLData(root.tag, tree.getpath(root), type=root_schema.type.name, max_occurs=root_schema.max_occurs, min_occurs=root_schema.min_occurs)'''