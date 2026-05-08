# Grupo 9: Teste de Qualidade (Linha de Produção)
#Problema: Verificar 10 peças. O usuário digita 1 para peça boa ou 0 para defeituosa.
#Detalhes: Ao final das 10 repetições, o programa deve dizer: "Total de peças aprovadas: [X]".
#Objetivo Técnico: Laço com número de repetições fixo (for) e um contador interno.
#Variáveis: peca_status, aprovadas, total_lote.

aprovadas = 0
total_lote = 10

for i in range(total_lote):
    peca_status = int(input(f"A peça {i + 1} é boa (1) ou defeituosa (0)? "))

    if peca_status == 1:
        aprovadas += 1

porcentagem = (aprovadas / total_lote) * 100

print("Total de peças aprovadas:", aprovadas)
print("Porcentagem de peças aprovadas:", porcentagem, "%")