#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato

preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))

maisbarato = preco1

if (preco2 < maisbarato):
    maisbarato = preco2
if (preco3 < preco2):
    maisbarato = preco3

print("Voce deve comprar o produto de valor:", maisbarato)