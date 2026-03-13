contador = 1 
soma_notas = 0

while contador <= 4:
    notas= float(input(f"Digite a nota do { contador } bimestre: "))
    if notas < 0 or notas > 10:
        print("nota inválida. A nota deve estar entre 0 e 10") 
        continue
    contador += 1  
    soma_notas += notas

media = soma_notas / 4
print("A média de notas é: ", media)
if media >= 7:
    print("O aluno está Aprovado")
if media>= 5:
    print("O aluno esta em recuperação")   
else:
    print("O aluno está Reprovado")
