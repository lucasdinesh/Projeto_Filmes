########### BUSCA DE NOME ########################
class TrieNode(object):

    def __init__(self, char: str, movieid=0):
        self.char = char
        self.children = []
        self.movieid = 0
        self.word_finished = False
        self.counter = 1
        self.folha = False


def add(root, word: str, movieid: int):

    node = root
    for char in word:
        found_in_child = False

        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child

                if node.folha == True:
                    node.folha = False

                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)

            node = new_node

    if len(node.children) == 0:
        node.folha = True

    node.movieid = movieid # Adiciona o campo movieID no ultimo caracter adicionado na arvore trie
    node.word_finished = True


def find_prefix(root, prefix: str):

    node = root

    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True

        for child in node.children:
            if child.char == char:

                char_not_found = False

                node = child
                break

        if char_not_found:
            return False, 0

    return True, node


def acha_o_resto (node, achados):

    if (node.movieid != 0):
        achados.append(node.movieid)
        if (node.folha == True):
            return

    for child in node.children:

        if (child.folha == True):
            achados.append(child.movieid)
            break

        if (child.counter != 0 ):
            aux = acha_o_resto(child, achados)
            if aux != 0:
                achados.append(aux)

    return child.movieid
