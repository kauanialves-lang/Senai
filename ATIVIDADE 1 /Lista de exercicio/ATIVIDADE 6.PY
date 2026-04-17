while True:
    peso_prato = float(input("Digite o peso do prato pelo cliente (em quilos)"))
    if peso_prato >=0:
        break
    print("Valor Invalido")

valor_a_pagar = peso_prato * 12.0
print ("Ovalor a pagar é de R$: ", valor_a_pagar)