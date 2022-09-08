#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
#Valide a entrada e permita repetir a operação.

pais_a = float (input('Digite a polulação do país A: '))
tx_a = float (input('Digite a taxa de crescimento do país A: '))/100
pais_b = float (input('Digite a polulação do país B: '))
tx_b = float (input('Digite a taxa de crescimento do país B: '))/100

ano = 0 #simular a passagem de anos
while (pais_a < pais_b):
#while pais_a < pais_b:
    pais_a = round(pais_a * tx_a + pais_a)
    pais_b = round(pais_b * tx_b + pais_b)
    ano = ano + 1

print(f'''
A população do País A de {pais_a} habitantes
ultrapassou o País B de {pais_b} habitantes
após {ano} anos.
''')
