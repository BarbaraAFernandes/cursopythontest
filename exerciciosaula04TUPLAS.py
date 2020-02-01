###Escreva uma tupla e valide se a mesma é um tipo de tupla utilizando o type.
###Escreva uma tupla com alterne as posições da mesma com o comando print.

"""
tupla_objetos = ('celular', 'copo', 'Mesa', 'computador')
print(type(tupla_objetos))
print(tupla_objetos)
print(tupla_objetos[0:3])

"""

###Escreva uma tupla com valores numéricos e retorne o menor valor da tupla.

"""
tupla_numeros = 1,15,36,45,56,87
print(min(tupla_numeros))

"""

###Utilize as tuplas existentes e concatene os dados das tuplas em uma 3 tupla.

tupla_objetos = ('celular', 'copo', 'Mesa', 'computador')
tupla_numeros = 1,15,36,45,56,87
print (tupla_numeros+tupla_objetos)

###Verifique se um valor está contido dentro da tupla utilizando condicionais if/else.

if 'celular' in tupla_objetos:
    print('Há este item na tupla')
else:
    print('Não há este item na tupla')
