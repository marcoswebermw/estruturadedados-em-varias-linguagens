## Listas Circulares
  
São listas onde o primeiro elemento tem um ponteiro para o último elemento, e o último elemento tem um ponteiro para o primeiro.  
  
São formadas por:  
  
* Dados;
* Ponteiro para o próximo elemento;
* Ponteiro para o elemento anterior;
* Se for o primeiro elemento, o ponteiro que indica o elemento anterior, apontará para o último elemento da lista;
* Se for o último elemento, o ponteiro que indica o próximo elemento, apontará para o primeiro elemento da lista;
  
Assim que um novo elemento for inserido, o último elemento terá seu campo próximo apontando para ele. E esse novo elemento receberá do elemento anterior o endereço do primeiro elemento da lista.  
  
