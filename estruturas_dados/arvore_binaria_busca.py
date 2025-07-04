from bintrees import AVLTree

class ArvoreBinariaBusca:
    def __init__(self):
        self._arvore_avl = AVLTree()

    def inserir(self, chave, valor):
        self._arvore_avl.insert(chave, valor)

    def buscar(self, chave):
        try:
            return self._arvore_avl.get(chave)
        except KeyError:
            return None

    def remover(self, chave):
        try:
            self._arvore_avl.remove(chave)
        except KeyError:
            pass

    def percurso_em_ordem(self):
        lista = []

        self._arvore_avl.foreach(lambda _,valor: lista.append(valor), 0)
        
        return lista        