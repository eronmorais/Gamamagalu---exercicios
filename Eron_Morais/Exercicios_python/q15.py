g_hora = float(input("Quanto você ganha por hora: "))
h_mes = float(input("Horas trabalhadas no mês: "))
salario_mes = g_hora * h_mes
ir = (salario_mes * 0.11)
inss = (salario_mes * 0.08)
sindicato = (salario_mes * 0.05)
salario_liq = (salario_mes - ir - inss - sindicato)

print("+ Salário Bruto : R$", salario_mes)
print("- IR (11%) : R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sindicato)
print("= Salário Liquido : R$", salario_liq)
