### DICIONARIOS ###

dicionario = {'chave': 'valor'}

###EXEMPLO DE DICIONARIOS:

frutas_iniciais = {'A': 'Abacate', 'M': 'Melancia', 'L':'Limão','B':'Banana'}
print(frutas_iniciais)


###Trazer uma parte do dicionario

"""
print(frutas_iniciais['M'])

"""

###Iterando em dicionarios:

"""
for dic in frutas_iniciais:
    print(dic + " " + frutas_iniciais[dic])

"""

###Somente os valores:

"""
for dic in frutas_iniciais.values():
    print(dic)

"""

###Somente as Chaves:

"""
for dic in frutas_iniciais.keys():
    print(dic)

"""


###Utilizando Tuplas com dicionários:

n_ruas = {
(100,200) : 'Rua do Braz',
(1,100): 'Rua das Arvores',
(50,230): 'Rua dos Atletas',
}
print(n_ruas)