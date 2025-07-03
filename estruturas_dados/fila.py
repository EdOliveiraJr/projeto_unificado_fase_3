# /estruturas_dados/fila.py

from collections import deque

class Fila:
    """
    Implementação de uma Fila (Queue) utilizando a estrutura de dados 'deque'
    da biblioteca padrão do Python, que é otimizada para operações de append e pop
    em ambas as extremidades.
    """
    def __init__(self):
        self._elementos = deque()

    def enfileirar(self, item):
        """
        Adiciona um item ao final da fila.
        - Complexidade de Tempo: O(1) - Operação de append em um deque é de tempo constante.
        - Complexidade de Espaço: O(1) - Apenas o espaço para o item é adicionado.
        """
        self._elementos.append(item)

    def desenfileirar(self):
        """
        Remove e retorna o primeiro item da fila.
        - Complexidade de Tempo: O(1) - Operação de popleft em um deque é de tempo constante.
        - Complexidade de Espaço: O(1).
        """
        if self.esta_vazia():
            return None
        return self._elementos.popleft()

    def esta_vazia(self) -> bool:
        """
        Verifica se a fila está vazia.
        - Complexidade de Tempo: O(1).
        - Complexidade de Espaço: O(1).
        """
        return len(self._elementos) == 0

    def __len__(self):
        return len(self._elementos)
