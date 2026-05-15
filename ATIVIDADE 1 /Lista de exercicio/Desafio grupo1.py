aprovadas = 0
total_lote = 10

for i in range(total_lote):
    peca_status = int(input(f"A peça {i + 1} é boa (1) ou defeituosa (0)? "))

    if peca_status == 1:
        aprovadas += 1

porcentagem = (aprovadas / total_lote) * 100

print("Total de peças aprovadas:", aprovadas)
print("Porcentagem de peças aprovadas:", porcentagem, "%")