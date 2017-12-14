# Começa a fazer o loop externo à partir do segundo item da lista.
# Pois a lógica do algoritmo é testar o sucessor com seus antecessores até encontrar um com 
# valor menor que ele ou até chegar à primeira posição da lista.
def insercao(lista):
    tamanho_lista = len(lista)
    for i in range(1, tamanho_lista):
        valor_temp = lista[i]
        posicao_anterior = i - 1

        # Verifica se a posição anterior não é negativa e se o valor testado é menor do que seu anterior.
        # Se as duas condições forem verdadeiras, o valor maior é escrito na posição da direita(antiga posição do valor_temp).
        # O valor_temp não é escrito imediatamente. Primeiro ele é testado com todos os elementos à 
        # esquerda(até encontrar algum menor ou igual a ele), e vai ficando mais à esquerda caso for menor que seus antecessores. 
        # Só é escrito quando o while for finalizado.
        while (posicao_anterior >= 0) and (valor_temp < lista[posicao_anterior]):
            lista[posicao_anterior+1] = lista[posicao_anterior]
            posicao_anterior = posicao_anterior-1
        
        lista[posicao_anterior+1] = valor_temp

    return lista



if __name__ == '__main__':
    lista = [4,3,5,1,2]
    print(insercao(lista))



