####  TUPLAS  #####

"""
tupla_numeros = (1,2,56,45)
print(type(tupla_numeros))
print(tupla_numeros)

tupla_numeros = 1,2,56,45
print(type(tupla_numeros))
print(tupla_numeros)
print(len(tupla_numeros))
print(tupla_numeros[2])

#tupla_numeros = (1,)
#print(type(tupla_numeros))
#print(tupla_numeros)

"""

###CALCULOS DENTRO DE TUPLAS###
###SUM SOMA OS VALORES DA TUPLA
##MAX MOSTRA O NUMERO MAX DE UM VALOR DENTRO DA TUPLA

#print(sum(tupla_numeros))
#print(max(tupla_numeros))

##Concatenação de tuplas (junção)

"""
tupla_numeros01 = 1,45,56,12
tupla_numeros02 = 2,23,78,0
print(tupla_numeros01+tupla_numeros02)
"""

###Soma de tuplas (criação de nova tupla)

"""
tupla_numeros01 = 1,45,56,12
tupla_numeros02 = 2,23,78,0

tupla_numero03 = sum(tupla_numeros01 + tupla_numeros02)
print(tupla_numero03)

"""
###SUBSTITUIÇÃO DE TUPLA, PASSANDO VALORES PARA OUTRA
### Verificar se um dados está contido na Tupla.

tupla_numeros01 = 1,45,56,12
tupla_numeros02 = 2,23,78,0

tupla_numeros = tupla_numeros01+tupla_numeros02
print(tupla_numeros)
print(45 in tupla_numeros)

###Iterando em Tuplas

"""
for i in tupla_numeros:
    print(i)

"""

###Para copiar os dados de uma tupla basta a nova tupla receber o valor da tupla existente.

copia_tupla_numeros = tupla_numeros
print(copia_tupla_numeros)




