salario = float(input("Digite seu salário Atual: "))
x = salario * 0.15
aumento = salario + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print("O salário sem aumento era: ", salario)
print("O salário com aumento ficou: ", aumento)
print("O salário final ficou: ", salariofinal)
