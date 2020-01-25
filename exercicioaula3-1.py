##Crie um programa que imprima na tela numero que começam de 0 até 100.
"""

for numeros in range(0,101):
    print (numeros)

"""
##Crie um algoritmo onde o mesmo percorre uma lista de nome de carros e
##imprima em tela os elementos da lista criada.
"""

carros = ["Mobi", "Palio", "Peugeot","F75"]
for c in carros: 
    print (c)

"""
##Crie uma lista com nome de Cidades onde contenha a cidade Florianópolis
## imprima em tela somente a cidade de Florianópolis da lista criada.
"""

cidades = ["Foz do Iguaçu", "Fortaleza", "Florianópolis", "Flórida"]
for c in cidades: 
    print(cidades[2])

"""
##Crie um algoritmo que faça a soma de 5 numero de uma lista com ele mesmo.
"""

for soma in [1,2,3,4,5]:
    print(soma + soma)

"""
##FUNÇÕES##
###Crie uma função que faça a soma de 3 números e imprima em tela o resultado da soma.
"""

def soma(a, b , c):
    return  a + b + c

d= soma(1,3,6)
print(d)

"""
### FUNÇOES###
###Crie uma algoritmo utilizando funções onde calcule o valor hora ganho de um funcionario
###Sendo que o valor hora devera ser um padrão nomeado.
###E o numero de horas trabalhadas deverá ser inserido pelo usuário.
###E imprima em tela o total ganho desse funcionário baseado nas horas trabalhadas.

def salario_final():
    hora = int(input('Quantas horas você trabalhou hoje? '))  
    valor_hora = 10
    multiplicar = hora * valor_hora 
    print(multiplicar)
    
salario_final()




###Crie um programa onde a função irá validar o nome e o CPF da pessoa estão
###corretos baseados nos dados apresentados. Valide com retornos em tela se o CPF
###está correto se o nome está correto.

"""
def validaCPF(nome, CPF):
    if nome == "Barbara" and CPF == "107.547.009-92" :
        return "CPF e nome Corretos Bem Vindos"
    elif nome == "Barbara":
        return "Usuário Correto"
    elif CPF == "107.547.009-92":
        return "CPF correta"
    else:
        return "Usuário ou CPF Incorretos"

print(validaCPF("Barbara","107.547.009-92"))

"""






