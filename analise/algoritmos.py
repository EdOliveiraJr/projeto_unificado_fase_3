# /analise/algoritmos.py

def insertion_sort(lista: list, key=lambda x: x, reverse: bool = False):
    """
    Implementação do Insertion Sort.
    - Complexidade de Tempo: O(n^2) no pior e médio caso. O(n) no melhor caso (lista já ordenada).
    - Complexidade de Espaço: O(1) - ordenação in-place.
    É eficiente para listas pequenas ou parcialmente ordenadas.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Compara a chave com cada elemento à sua esquerda
        # A condição de comparação muda com base no parâmetro 'reverse'
        while j >= 0 and (key(chave) > key(lista[j]) if reverse else key(chave) < key(lista[j])):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def quick_sort(lista: list, key=lambda x: x, reverse: bool = False):
    """
    Implementação do Quick Sort.
    - Complexidade de Tempo: O(n log n) no caso médio e melhor. O(n^2) no pior caso.
    - Complexidade de Espaço: O(log n) a O(n), dependendo da implementação e do balanceamento das partições.
    Geralmente mais rápido que outros algoritmos O(n^2) para grandes volumes de dados.
    """
    if len(lista) <= 1:
        return lista
    else:
        # Escolha do pivô (aqui, o elemento do meio)
        pivo = lista[len(lista) // 2]
        
        # Particiona a lista com base no pivô
        menores = [x for x in lista if key(x) < key(pivo)]
        iguais = [x for x in lista if key(x) == key(pivo)]
        maiores = [x for x in lista if key(x) > key(pivo)]

        # A ordem da concatenação final depende do parâmetro 'reverse'
        if reverse:
            return quick_sort(maiores, key=key, reverse=reverse) + iguais + quick_sort(menores, key=key, reverse=reverse)
        else:
            return quick_sort(menores, key=key, reverse=reverse) + iguais + quick_sort(maiores, key=key, reverse=reverse)

