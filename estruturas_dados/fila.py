from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()
    
    def estaVazia(self):
        return self.fila.count() == 0
    
    def enfileirar(self, linha_csv):
        self.fila.append(linha_csv)

    def desenfileirar(self):
        return self.fila.popleft()
