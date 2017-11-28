type_compatibility = [[1.0],
                      [0.0, 1.0],
                      [0.6, 0.4, 1.0],
                      [0.6, 0.4, 0.8, 1.0],
                      [0.6, 0.4, 0.8, 0.8, 1.0],
                      [0.8, 0.0, 0.6, 0.6, 0.6, 1.0],
                      [0.8, 0.6, 0.6, 0.6, 0.6, 0.8, 1.0],
                      [0.0, 0.0, 0.6, 0.6, 0.6, 0.8, 0.6, 1.0],
                      [0.0, 0.0, 0.4, 0.4, 0.4, 0.8, 0.6, 0.8, 1.0],
                      [0.0, 0.0, 0.4, 0.4, 0.4, 0.0, 0.0, 0.0, 0.0, 1.0],
                      [0.0, 0.0, 0.4, 0.4, 0.4, 0.0, 0.0, 0.0, 0.0, 0.8, 1.0],
                      [0.0, 0.0, 0.4, 0.4, 0.4, 0.0, 0.0, 0.0, 0.0, 0.8, 0.8, 1.0],
                      [0.0, 0.0, 0.6, 0.4, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

cardinality_compatibility = [[1.0],
                             [0.9, 1.0],
                             [0.7, 0.7, 1.0],
                             [0.7, 0.7, 0.8, 1.0]]


def map_type(data_type):
    data_type = data_type.lower()
    return {
        '*': 0,
        '+': 1,
        '?': 2,
        'none': 3,
        'boolean': 1,
        'char': 3,
        'character': 3,
        'string': 4,
        'number': 5,
        'int': 6,
        'integer': 6,
        'float': 7,
        'double': 7,
        'date': 10,
        'time': 11,
        'datetime': 9,
        'real': 7,
        'bit': 1,
        'distinct': 0,
        'bigint': 6,
        'smallint': 6,
        'tinyint': 6,
        'decimal': 8,
        'numeric': 8,
        'timestamp': 9,
        'varchar': 4,
        'longvarchar': 4,
        'binary': 13,
        'varbinary': 13,
        'longvarbinary': 13,
        'clob': 4,
        'blob': 13,
        'id': 0,
        'idref': 0,
        'idrefs': 12,
        'nmtoken': 2,
        'nmtokens': 12,
        'enumeration': 12,
        'cdata': 4,
        'uri': 0,
        'anyuri': 0,
        'normalizedstring': 4,
        'bin': 13,
        'fixed': 8,
        'nvarchar': 4,
        'nchar': 3,
        'ntext': 4,
        'money': 8,
        'image': 13,
        'identity': 6
    }.get(data_type, 14)


def get_data_type_similarity(data_type1, data_type2):
    sim = 0
    if data_type1 is None or data_type2 is None:
        return sim
    type_id1 = map_type(data_type1)
    type_id2 = map_type(data_type2)
    if type_id1 > type_id2:
        return type_compatibility[type_id1][type_id2]
    else:
        return type_compatibility[type_id2][type_id1]

def get_cardinality_similarity(dc1, dc2):
    sim = 0
    if dc1 is None or dc2 is None:
        return sim
    card_id1 = map_type(dc1)
    card_id2 = map_type(dc2)
    if card_id1 > card_id2:
        return cardinality_compatibility[card_id1][card_id2]
    else:
        return cardinality_compatibility[card_id2][card_id1]


if __name__ == "__main__":
    print(get_data_type_similarity("String", "Int"))
    print(get_data_type_similarity("String", "float"))
    print(get_data_type_similarity("float", "double"))
    print(get_data_type_similarity("String", "char"))
    print(get_cardinality_similarity("?", "none"))
