
def merge_sort(lista, chave):
    # listas com zero ou um elemento já estão ordenadas.
    if len(lista) <= 1:
        return lista[:]

    # Divide a lista ao meio.
    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    # Junta as duas partes ordenadas.
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if chave(esquerda[i]) >= chave(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos que sobraram.
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
