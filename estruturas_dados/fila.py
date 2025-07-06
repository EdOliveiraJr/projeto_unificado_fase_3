from collections import deque

class Fila:
    """
    Implementação de uma Fila (Queue) utilizando a estrutura de dados 'deque'
    da biblioteca padrão do Python, que é otimizada para operações de append e pop
    em ambas as extremidades.
    """
    def __init__(self):
        self.fila = deque()
    
    def esta_vazia(self):
        return self.fila.__len__() == 0
    """
    Adiciona um item ao final da fila.
    - Complexidade de Tempo: O(1) - Operação de append em um deque é de tempo constante.
    - Complexidade de Espaço: O(1) - Apenas o espaço para o item é adicionado.
    """
    def enfileirar(self, linha_csv):
        self.fila.append(linha_csv)
    """
    Remove e retorna o primeiro item da fila.
    - Complexidade de Tempo: O(1) - Operação de popleft em um deque é de tempo constante.
    - Complexidade de Espaço: O(1).
    """
    def desenfileirar(self):
        return self.fila.popleft()