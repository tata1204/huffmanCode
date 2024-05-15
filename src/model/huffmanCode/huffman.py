from collections import Counter

class NodeTree(object):
    def __init__(self, left=None, right=None):
        """
        Constructor de la clase NodeTree.
        """
        self.left = left
        self.right = right

    def children(self):
        """
        Método para obtener los hijos del nodo.
        """
        return self.left, self.right

    def __str__(self):
        """
        Método para obtener una representación en cadena del nodo.
        """
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    '''
    Función para encontrar el Código Huffman.
    '''
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


def make_tree(nodes):
    '''
    Función para construir el árbol de codificación Huffman.
    '''
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


def decode_message(encoded: str, encoding_dict=None) -> str:
    '''
    Función para decodificar un mensaje codificado.
    '''
    if encoding_dict is None:
        return "No se ha codificado ningún mensaje, no se puede decodificar."

    if isinstance(encoding_dict, str):
        try:
            encoding_dict = eval(encoding_dict.replace("'", "\""))
        except SyntaxError:
            return "Se debe codificar primero."

    cache = ""
    decoded = ""

    start = 0
    for end in range(1, len(encoded) + 1):
        sub_str = encoded[start:end]
        for char, code in encoding_dict.items():
            if sub_str == code:
                decoded += char
                start = end
                break

    return decoded



def encode_message(message):
    '''
    Función para codificar un mensaje codificado.
    '''
    message = message.strip()
    encoded_output = ""
    dictionary_output = ""
    
    if message:
        if len(message) == 1:
            encoded_output = '1'
            dictionary_output = "{'" + message + "': '1'}"
        else:
            freq = dict(Counter(message))
            freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
            node = make_tree(freq)
            encoding = huffman_code_tree(node)

            encoded_output = ''
            for char in message:
                encoded_output += encoding[char]

            dictionary_output = encoding
    else:
        encoded_output = "¡Ingrese un mensaje para codificar!"

    return encoded_output, dictionary_output