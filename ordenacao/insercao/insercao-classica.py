# Só uma forma mais comum de encontrar este algoritmo.
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i-1
        while j>=0 and chave < lista[j]:
            lista[j+1] = lista[j]
            j = j-1
        lista[j+1] = chave


if __name__ == '__main__':
    lista = [21,53,81,14,5]
    print('Lista Desordenada: {}'.format(lista))
    insertion_sort(lista)
    print('Lista Ordenada: {}'.format(lista))
