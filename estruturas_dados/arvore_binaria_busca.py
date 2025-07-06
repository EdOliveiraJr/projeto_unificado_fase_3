from bintrees import AVLTree


class ArvoreBinariaBusca:
    """
    Implementação de uma Árvore de Busca Binária (Binary Search Tree - BST)
    utilizando uma Árvore AVL da biblioteca 'bintrees' como base.
    A AVL Tree é auto-balanceada, garantindo que as operações de busca, inserção
    e remoção tenham uma complexidade de tempo logarítmica.
    """

    def __init__(self):
        self._arvore_avl = AVLTree()

    """
    Insere um par chave-valor na árvore.
    - Complexidade de Tempo: O(log n) - Graças ao auto-balanceamento da AVL.
    - Complexidade de Espaço: O(log n) - Para a recursão da inserção.
    """

    def inserir(self, chave, valor):
        self._arvore_avl.insert(chave, valor)

    """
    Busca um valor na árvore a partir de uma chave.
    - Complexidade de Tempo: O(log n) - Graças ao auto-balanceamento da AVL.
    - Complexidade de Espaço: O(log n) - Para a recursão da busca.
    """

    def buscar(self, chave):
        try:
            return self._arvore_avl.get(chave)
        except KeyError:
            return None

    """
    Remove um nó da árvore a partir de uma chave.
    - Complexidade de Tempo: O(log n) - Graças ao auto-balanceamento da AVL.
    - Complexidade de Espaço: O(log n).
    """

    def remover(self, chave):
        try:
            self._arvore_avl.remove(chave)
        except KeyError:
            pass

    """
    Retorna uma lista com todos os valores da árvore em ordem de chave.
    - Complexidade de Tempo: O(n) - É necessário visitar todos os 'n' nós da árvore.
    - Complexidade de Espaço: O(n) - Para criar a lista com todos os valores.
    """

    def percurso_em_ordem(self):
        lista = []

        self._arvore_avl.foreach(lambda _, valor: lista.append(valor), 0)

        return lista
