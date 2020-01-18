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
'''
num1 = int(input("Digite o Primeiro numero"))
num2 = int(input("Digite o segundo numero"))


if num1 > num2:
    print('Numero 1 maior que Numero 2')
elif num1 == num2:
    print('Numeros Iguais')
elif num2 != num1:
    print('Numeros diferentes')
else:
    print('Numero 2 maior que Numero 1')
'''
#condicionais e portas logicas
'''
num1 = int(input("Digite o Primeiro numero"))
num2 = int(input("Digite o segundo numero"))

if num1 > num2:
    print('Numero 1 maior que Numero 2')
elif num1 == 10 and num2 == 10:
    print('Numero restrito')
else:
    print('Numero 2 maior que Numero 1')

    '''
#Exercicios aula 02
#Escrever um programa onde você entra com 3 notas de 1 há 10
#e calcula a média dessas notas.

'''
nota1 = int(input('1 prova '))
nota2 = int(input('2 prova '))
nota3 = int(input('3 prova'))

TotalNota = (nota1+nota2+nota3)
MediaNota = TotalNota/3

print(TotalNota,MediaNota)

Media = (nota1 + nota2 + nota3)/3
if Media >= 7:
    print('Aluno aprovado')
elif Media >= 5:
    print('em recuperação')
elif Media >= 6:
    print('em recuperação')
else:
    print('Aluno reprovado')

'''

#Escrever um programa Sinaleira
#Se escrever verde, retorna em: Passar. 
#Se escrever amarelo, retorna em : Atenção vai parar.
#Se escrever vermelho, retorna em: Parar.
#Se escrever qualquer outra cor, escrever: Isso não é uma cor da sinaleira. 

cor = input('digite cor')


#Cores = (cor1,cor2,cor3)

if cor == "verde":
    print('Pode Passar!')
elif cor == 'amarelo':
    print('Vai parar!')
elif cor == 'vermelho':
    print('Parar!')
else:
    print('Isso não é uma cor da sinaleira')




 

