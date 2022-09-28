#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
#Por exemplo: 127 -> 721

def conversao(hora, minuto): #horas:minutos
    if hora == 0:#a.m
        return str(12) + ':' + str(minutos)
    elif hora <= 12 :#1-11 a.m e 12p.m
        return str(hora) + ':' + str(minutos)
    else:#13-23p.m.
        return str(hora-12) + ':' + str(minutos)

def converteTurno(hora):
    if hora >= 12: #12-23
        return 'P'
    else: #0-11
        return 'A'

def saida(turno):
    if turno == 'A': #A
        return 'A.M.'
    else: #P
        return 'P.M.'

opcao = ''
while opcao != 's': # até enquanto a opção for diferente de 's'
    horas = int(input('Horas: '))
    minutos = int(input('Minutos: '))

    horario = conversao(horas, minutos) #horas:minutos
    turno = converteTurno(horas) # 'A' ou 'P'
    turno = saida(turno) # 'A.M.' ou 'P.M.'

    print(horario + ' ' + turno) #horas:minutos turno
    opcao = input('Continuar - Enter , Sair - s').lower()

print('Fim do Programa!')