from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()
    
    def esta_vazia(self):
        return self.fila.__len__() == 0
    
    def enfileirar(self, linha_csv):
        self.fila.append(linha_csv)

    def desenfileirar(self):
        return self.fila.popleft()
