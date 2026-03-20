
preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pagamento = float(input("Digite o valor que deseja pagar: "))

litros = valor_pagamento / preco_litro

print(f"Você conseguiu colocar {litros:.2f} litros de gasolina.")

