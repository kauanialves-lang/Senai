nome = input("insira nome do aluno")
nota1=float(input("insira primeira nota:"))
nota2=float(input("insira segunda nota:"))
media=(nota1 + nota2) /2
print("A média das notas é:",media)
if media >= 7:
    print("O aluno está Aprovado")
else:
    print("O aluno está Reprovado")