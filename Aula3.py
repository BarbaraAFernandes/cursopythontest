#Estrutura de Repetições.
#Laços While.


"""
numero = 0
while numero <= 10:
    print (numero)
    numero = numero + 1

numero = 0
while numero <= 10:
    print (numero)
    numero = numero + 1
else:
    print('Acabou o laço While')

"""
"""

##Looping infinito
numero = 0
while numero <=10:
    print(numero)
    break

## tabuada

tabuada = int(input("Insira o numero da tabuada"))

multiplicador = 1
if tabuada > 10:
    print('Digite numeros até 10')
    else:
    while (multiplicador <= 10):
        print(tabuada * multiplicador )

multiplicador = multiplicador + 1

else:
        print("Fim da Tabuada de ",tabuada)

"""

##Laços de repetição FOR
##primeira estrutura de dados lista se escreve com [] e virgulas.

#Estrutura de dados chamada Lista

"""
frutas = ["Manga" , "Pera" , "Uva" , "Morango"]
for f in frutas:
    print(f)

"""
## Gerou um range de numeros
"""
for intervalonumeros in range(10,20):
    print(intervalonumeros)

"""
## Listou as strings
"""
nome = "Barbara Alessandra"
for letras in nome:
    print(letras)

"""
##Enumerar indices
"""
frutas = ['Manga', 'Pera', 'Uva', 'Morango', 'Maçã','Limão ']
for f, frutas in enumerate(frutas):
    print(f, frutas)

"""
##iterou a posição 2 por ter feito o loop 4 vezes.
"""
frutas = ['Manga', 'Pera', 'Uva', 'Morango']
for f in frutas:
    print(frutas[2])

"""

##Itera as strings da lista 
"""
frutas = ['Manga', 'Pera', 'Uva', 'Morango']
for f in frutas:
    print(f[0:4])

"""

##multiplicação

"""
for multiplicacao in [1,2,3,4,5]:
    print(multiplicacao*10)

"""




