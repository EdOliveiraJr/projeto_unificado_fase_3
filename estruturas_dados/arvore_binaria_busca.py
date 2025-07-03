# # /estruturas_dados/arvore_binaria_busca.py

# from bintrees import AVLTree

# class ArvoreBinariaBusca:
#     """
#     Implementação de uma Árvore de Busca Binária (Binary Search Tree - BST)
#     utilizando uma Árvore AVL da biblioteca 'bintrees' como base.
#     A AVL Tree é auto-balanceada, garantindo que as operações de busca, inserção
#     e remoção tenham uma complexidade de tempo logarítmica.
#     """
#     def __init__(self):
#         self._arvore = AVLTree()

#     def inserir(self, chave, valor):
#         """
#         Insere um par chave-valor na árvore.
#         - Complexidade de Tempo: O(log n) - Graças ao auto-balanceamento da AVL.
#         - Complexidade de Espaço: O(log n) - Para a recursão da inserção.
#         """
#         self._arvore.insert(chave, valor)

#     def buscar(self, chave):
#         """
#         Busca um valor na árvore a partir de uma chave.
#         - Complexidade de Tempo: O(log n) - Graças ao auto-balanceamento da AVL.
#         - Complexidade de Espaço: O(log n) - Para a recursão da busca.
#         """
#         return self._arvore.get(chave)

#     def remover(self, chave):
#         """
#         Remove um nó da árvore a partir de uma chave.
#         - Complexidade de Tempo: O(log n) - Graças ao auto-balanceamento da AVL.
#         - Complexidade de Espaço: O(log n).
#         """
#         if chave in self._arvore:
#             del self._arvore[chave]

#     def percurso_em_ordem(self) -> list:
#         """
#         Retorna uma lista com todos os valores da árvore em ordem de chave.
#         - Complexidade de Tempo: O(n) - É necessário visitar todos os 'n' nós da árvore.
#         - Complexidade de Espaço: O(n) - Para criar a lista com todos os valores.
#         """
#         # O método items() da AVLTree já retorna os itens em ordem de chave.
#         return [valor for chave, valor in self._arvore.items()]

#     def __len__(self):
#         return len(self._arvore)

try:
    from bintrees import AVLTree
except ImportError:
    print("Biblioteca 'bintrees' não encontrada. Instale com: pip install bintrees")
    AVLTree = dict 

class ArvoreBinariaBusca:
    def __init__(self):
        self._arvore_avl = AVLTree()
    def inserir(self, chave, valor):
        self._arvore_avl.insert(chave, valor)
    def buscar(self, chave):
        return self._arvore_avl.get(chave)
    def remover(self, chave):
        if chave in self._arvore_avl:
            del self._arvore_avl[chave]
    def percurso_em_ordem(self):
        return [valor for chave, valor in self._arvore_avl.items()]
    def __len__(self):
        return len(self._arvore_avl)
    def esta_vazia(self):
        return len(self) == 0
