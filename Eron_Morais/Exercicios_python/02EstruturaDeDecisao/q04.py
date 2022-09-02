#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = input("Digite uma letra: ")

if (letra in ('aeiou') or letra in ('AEIOU')):
    print ("É vogal")
else:
    print("É consoante")