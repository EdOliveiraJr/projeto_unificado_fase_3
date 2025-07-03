class Fila:
    def __init__(self):
        self.items = []
    
    def estaVazia(self):
        return self.items == []
    
    def enfileirar(self, linha_csv):
        self.items.insert(0, linha_csv)

    def desenfileirar(self):
        return self.items.pop()
