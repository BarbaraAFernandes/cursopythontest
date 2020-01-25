##imprimir em tela todas as datas que ocorreram as
##olimpíadas em um período de 4 em 4 anos.

'''
anoinicio = int(input('Digite inicio'))
anofim = int(input('Digite fim'))

while (anoinicio <= anofim):
    print(anoinicio)
    anoinicio = anoinicio +4
print('Esses foram os anos da olimpiada até',anofim)
'''

##Escrever um programa que faça o incremento de 500 reais no valor final do
##salário sendo que o incremento será de 100 reais até totalizar os 500 reais.

sal_ini = int('Insira o Salario Inicial'))
sal_final = sal_ini + 500

while(sal_ini <= sal_final):
    print(sal_ini)
    sal_ini = sal_ini + 100
else:
    print(' O seu salario final é:', sal_final)

