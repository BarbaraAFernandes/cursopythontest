##Sorteador de numero##

import random
import math
"""
numero = random.randint(0,100)
print(numero)
"""

### lista ###

"""
lista = [1,45,56,43,21]
numero = random.choice(lista)
print(numero)

"""

### calculos matematicos modulo math

"""
print(math.pi)
print(math.sqrt(100))

"""

##Modulos Importados
##matplotlib. emulador de gráfico
##pandas é responsavel por analise de dados
## X =  é a variavel responsável por abrir o arquivo do excell

"""
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"C:\temp\teste.xlsx")
plt.hist(x["Quantidade"])
plt.hist(x["Material Escolar"])
plt.show()

"""

###Importar o módulo padrão do Python chamado date e testar na IDE se o mesmo
###Carregou as opções do modulo. Utilize a opção datetime.now() e print a data e hora na saída.

"""
import datetime
data_hora = datetime.datetime.now()
print(data_hora)

"""

###Importar a biblioteca externa chamada pypdf2 com comando pip, e importar a mesma
#Na IDE e testar as opções da mesma com o atributo PdfFileReader e print na tela
#o resultado desse atributo.

### informa class ###

"""
import PyPDF2

arquivo = PyPDF2.PdfFileReader
print(arquivo)

"""

##Estrutura de Dados
### LISTAS ###

lista_numeros = [100,23,34,56,67,13,58]
lista_carros = ['Mercedes','Opala','Brasilia','Ferrari','Fiat 147']
lista_mista = ['Mercedes',23,'Brasilia',45,'Fiat 147']

print(lista_numeros)
print(lista_carros)
print(lista_mista)

###TAMANHO da lista se usa LEN

#tamanho_lista = len(lista_mista)
#print(tamanho_lista)

###append = ADICIONA um item á lista
lista_mista.append("OPALA")
print(tamanho_lista)

### EXCLUI itens da lista

#del lista_numeros[4:6]
#print(lista_numeros)

###EXCLUI A LISTA COMPLETA:

#del lista_mista[:]
#print(lista_mista)

## PERCORRER A LISTA COM FOR:

##for lista_carros in lista_carros:
#print(lista_carros)

###ORDENAR ITENS DA LISTA:
"""
lista_numeros.sort()
print(lista_numeros)



lista_carros.sort()
print(lista_carros)

lista_carros.reverse()
print(lista_carros)

### REVERTE a lista:

lista_numeros.reverse()
print(lista_numeros)

"""




