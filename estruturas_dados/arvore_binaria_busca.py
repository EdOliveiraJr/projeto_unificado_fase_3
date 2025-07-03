from bintree import BinaryNode
from avltree import AVLTree

class ArvoreBinariaBusca:
    def __init__(self):
        self._arvore_avl = AVLTree()

    def inserir(self, chave, valor):
        self._arvore_avl.insert(chave, valor)

    def buscar(self, chave):
        try:
            return self._arvore_avl.search(chave)
        except KeyError:
            return None

    def remover(self, chave):
        try:
            self._arvore_avl.remove(chave)
        except KeyError:
            pass

    def percurso_em_ordem(self):
        return self._arvore_avl.in_order()