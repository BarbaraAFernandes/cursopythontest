#Crie um programa que faça multiplicação de dois valores, passando os valores em variáveis.
'''
num1 = 5
num2 = 10
print(num1+num2)
'''
#Crie um programa que valide se 2 numeros são maiores ou menor passando as condiçoes no terminal. (thrue or False)
'''
num1 = 9
num2 = 7

print(num1 >=7 or num2< num1)
print(num2 == num1 and num1 > num2)
'''
#Crie um programa que o usuário entre com o valor, o mesmo retorne me tela. O tipo de valor deverá ser FLOAT.
'''
num1 = 10.8
num2 = 15.1
num3 = 10.11

num1= float(input(num1))
num2= float(input(num2))
num3= float(input(num3))

print(num1+num2*num3)
'''

#Crie um programa que o usuário passe o valor de 3 notas e o mesmo calcule o total das notas e médias das notas. 
#Imprima em tela o total das notas e médias.
'''
nota1 = int(input('1 prova '))
nota2 = int(input('2 prova '))
nota3 = int(input('3 prova'))

TotalNota = (nota1+nota2+nota3)
MediaNota = TotalNota/3

print(TotalNota,MediaNota)

Media = (nota1 + nota2 + nota3)/3
if Media >= 7:
    print('aprovado')
else:
    print('vai para a prova final')

    '''
 ### Trabalhar com condicionais.

num1 = int(input("Digite o Primeiro numero"))
num2 = int(input("Digite o segundo numero"))


if num1 > num2:
    print('Numero 1 maior que Numero 2')
elif num1 == num2:
    print('Numeros Iguais')
else:
    print('Numero 2 maior que Numero 1')
