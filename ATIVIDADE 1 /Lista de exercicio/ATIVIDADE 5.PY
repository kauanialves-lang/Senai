preco_litro = float(input("Digite o preço do litro da gasolina: R$ "))
valor_pagamento = float(input("Digite o valor pago: R$ "))

litros = valor_pagamento / preco_litro

print(f"Quantidade de litros abastecidos: {litros:.2f} L")