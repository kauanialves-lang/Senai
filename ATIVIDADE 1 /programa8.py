nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while True: 
    if idade > 120 or idade < 0:
        print("Idade inválida! por favor, digite um valor menor ou igual a 120.")
        idade = int(input("Digite sua idade: "))
    else:
        break
dias_de_vida = idade * 365
print(f"Olá {nome}, voce já viveu cerca de: {dias_de_vida}")    