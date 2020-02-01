#Crie uma lista mista e conte o tamanho dessa lista.

lista_bebidas = ["Água", "Suco", "Refrigerante", "Chás", "Café"]
tamanho_lista = len(lista_bebidas)
print(tamanho_lista)

###Cria uma lista de dados do tipo string e adicione mais 2 valores
##nessa lista e printe o resultado dessa lista.

lista_artistas = ["Ariana Grande", "Beyoncé", "Dua Lipa", "AnaVitoria"]
lista_artistas.append(["SOAD", "Blackpink"])
print(lista_artistas)

##Percorra com laço for a lista mista criada criada anteriormente.
"""
for lista_artistas in lista_artistas:
    print(lista_artistas)
"""
###Remova o ultimo valor de dados da lista mista criada.
"""
del lista_bebidas[3:5]
print(lista_bebidas)
"""
###Ordene por ordem crescente e decrescente a lista de strings criada anteriormente.

lista_bebidas.sort()
print(lista_bebidas)

###Com condicionais faça com o que o usuário digite o valor de
###uma lista e o mesmo retorne se o valor digitado está dentro da lista ou não.

if "Ariana Grande" in lista_artistas:
    print("Este item está na lista")
else:
    print("Esse item não está na lista")




