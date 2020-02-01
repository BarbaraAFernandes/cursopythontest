### DICIONARIOS ###

dicionario = {'chave': 'valor'}

###EXEMPLO DE DICIONARIOS:

"""

frutas_iniciais = {'A': 'Abacate', 'M': 'Melancia', 'L':'Limão','B':'Banana'}
print(frutas_iniciais)

"""

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

###ADICIONANDO Dados há um dicionario
n_ruas[(200,500)] = 'Rua das Camelias'
print(n_ruas)

##REMOVENDO Dados de um dicionario:

"""
del n_ruas[(1,100)]
print(n_ruas)

"""
###Atualizando um dicionario atraves de outro dicionario
###Sobrescrever o dicionario

"""
nova_rua = { (201,500) : 'Rua José da Silva'}

n_ruas.update(nova_rua)
print(n_ruas)

"""

###Extrair informações de dicionários com pop
### Traz apenas a chave A. (Cada porta tem sua chave)

"""
frutas_iniciais = {'A': 'Abacate', 'M': 'Melancia', 'L':'Limão','B':'Banana'}
print(frutas_iniciais)

print(frutas_iniciais.pop('A'))

"""
###Limpar dados de um dicionário

"""
frutas_iniciais.clear()
print(frutas_iniciais)

"""


###Podemos copiar um dicionário dentro de outro dicionário utilizando COPY

#novas_ruas = n_ruas.copy()
novas_ruas = n_ruas
print(novas_ruas)

