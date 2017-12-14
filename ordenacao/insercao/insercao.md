## Ordenação por inserção - Insertion-sort
  
Algoritmo que é eficiente quando for ordenar um grupo de elementos pequenos. Mas é lento com uma grande quantidade de elementos.  
  

### Funcionamento
  
Um elemento é escolhido e é comparado com os seus anteriores.  
Os elementos maiores que ele serão colocados um-a-um na posição à direita de onde se encontravam.  
O nosso elemento, só para de ser comparado quando encontrar um elemento menor que ele.  
Então nosso elemento será inserido ao lado direito do elemento menor que ele.    
Depois o seguinte valor é comparado com seus anteriores. Isso ocorre até chegar na última posição da lista de elementos.  
  
### Passo-a-passo
  
1. Começa selecionando o segundo elemento para ser testado(`chamado aqui de sucessor`);
2. Armazena o valor `sucessor` em uma variável temporária(`temp` ou `key` ...);
3. Testa `temp` com seu o antecessor(à esquerda);
    1. Se `temp` for menor, coloca o valor do `antecessor` na posição imediatamente à sua direita;
    2. Se `temp` for maior, mantém `temp` na posição da direita em relação a seu `antecessor`. Depois reatribui `temp` com o valor do item à esquerda(`antecessor`) se houver;
4. O processo `3` vai ocorrendo até atingir os limites da lista.  

 ### Referências
   
* [Wikipedia](https://pt.wikipedia.org/wiki/Insertion_sort)   
* [Youtube](https://www.youtube.com/watch?v=RWRbhe81Ujg&feature=youtu.be&t=153)
* [Youtube 2](https://www.youtube.com/watch?v=6Kx2QV1r3p8)