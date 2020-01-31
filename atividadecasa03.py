##Crie uma lista de compras informando os produtos nessa lista
##imprimindo os itens de compra na tela utilizando a posição e o índice da mesma.

"""
compras = ['Arroz', 'Feijão', 'Macarrão', 'Verduras', 'Frutas', 'Legumes']
for c, compras in enumerate(compras):
    print(c, compras)

"""

##crie uma lista com valores onde o usuário deverá digitar um numero. 
##Se esse numero estiver na lista. Retorne ""Parabéns você acertou".
##Caso não esteja retorne " Você errou tente Novamente"
"""
def lista_numeros():
    valores = input('Insira um numero')
    numero = ["1","3","5", "7","9","11"]
    if valores in numero:
        print ("Parabéns, você acertou!")
    else:
        print("Voce errou, tente novamente")   

lista_numeros()

"""
##Crie uma função que receba 2 números. 
##O primeiro é um valor numérico e o segundo um percentual (ex. 10%).
## Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.

def soma(a, b):
    return  (a)+ (b /100*10)

c= soma(100,50)
print(c)




