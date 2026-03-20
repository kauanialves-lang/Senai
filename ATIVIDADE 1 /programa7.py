quant_pao = int(input("Digite a quantidade de pão vendidos: "))
quant_broa = int(input("Digite a quantidade de broa vendidos: "))

arrecadado = (quant_pao * 0.12) + (quant_broa * 1.50)
poupança = (arrecadado * 0.10)

print("Total de vendas de pão e broas foi: ", arrecadado)
print("Quantidade e dinheiro que ira para poupança: ",poupança)
