def quick_sort(lista, chave):
    """
    Implementação do Quick Sort para ordenar uma lista de objetos.

    Args:
        lista (list): A lista de objetos a ser ordenada.
        chave (function): Uma função lambda para extrair a métrica de 
                          comparação de cada objeto.
                          Ex: lambda c: c.calcular_tempo_total_consumo()
    
    Complexidade de Tempo:
        - Pior Caso: O(n^2) - Ocorre quando o pivô escolhido é sempre o menor
          ou o maior elemento, levando a partições desbalanceadas.
        - Caso Médio/Melhor Caso: O(n log n) - Ocorre quando o pivô divide
          a lista em partições de tamanhos próximos.

    Complexidade de Espaço:
        - O(n) - Esta implementação não é "in-place", pois cria novas listas 
          ('menores' e 'maiores') para o particionamento. Em cenários de 
          recursão profunda, o espaço pode ser proporcional a n.
    """
    if len(lista) <= 1:
        return lista
    else:
        # Escolhendo o pivô como o elemento do meio para um caso médio melhor
        pivo_index = len(lista) // 2
        pivo = lista[pivo_index]
        
        # Extrai o valor da métrica do pivô
        valor_pivo = chave(pivo)

        # Particiona a lista (list comprehensions criam novas listas)
        menores = [x for i, x in enumerate(lista) if i != pivo_index and chave(x) <= valor_pivo]
        maiores = [x for i, x in enumerate(lista) if i != pivo_index and chave(x) > valor_pivo]

        # Chamadas recursivas
        return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

def insertion_sort(lista, chave):
    """
    Implementação do Insertion Sort. Útil para listas pequenas ou quase ordenadas.
    Como mencionado pelo professor, é um algoritmo mais simples de implementar.

    Complexidade de Tempo:
        - Pior Caso/Caso Médio: O(n^2) - Ocorre quando a lista está em ordem
          inversa.
        - Melhor Caso: O(n) - Ocorre quando a lista já está ordenada.

    Complexidade de Espaço:
        - O(1) - É um algoritmo "in-place", ou seja, ordena a lista
          utilizando uma quantidade constante de espaço adicional.
    """
    # Itera do segundo elemento até o final da lista
    for i in range(1, len(lista)):
        item_atual = lista[i]
        valor_item_atual = chave(item_atual)
        j = i - 1
        
        # Move os elementos que são maiores que o item_atual para a direita
        while j >= 0 and chave(lista[j]) > valor_item_atual:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insere o item_atual em sua posição correta
        lista[j + 1] = item_atual
    return lista
