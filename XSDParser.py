import xmlschema

def demo():
    schema = xmlschema.XMLSchema('/home/fernandoms/xml-schemas/examples/currency/BookCatalogue2.xsd')
    elements = schema.findall('//*')
    print (elements)
    for element in elements:
        print (element.name)
        print (element.type)


if __name__ == "__main__":
    demo();