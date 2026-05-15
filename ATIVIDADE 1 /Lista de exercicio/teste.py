# =========================================
# SISTEMA DE TESTE DE QUALIDADE
# Integrantes: Pablo, Kauani e Veronica
# =========================================

# Mensagem de boas-vindas
print("========================================")
print(" BEM-VINDO AO SISTEMA DE QUALIDADE ")
print("========================================")

print("\nIntegrantes do grupo:")
print("- Pablo")
print("- Kauani")
print("- Veronica")

print("\nO sistema irá analisar 10 peças do lote.\n")

# Variáveis de controle
aprovadas = 0
defeituosas = 0

# -----------------------------------------
# Utilizamos o laço FOR porque sabemos
# exatamente a quantidade de repetições:
# serão analisadas 10 peças.
# -----------------------------------------

for i in range(10):

    while True:

        # Entrada de dados do operador
        status = input(f"Digite o estado da peça {i + 1} (1 = aprovada / 0 = defeituosa): ")

        # Verifica se o valor digitado é válido
        if status == "1" or status == "0":
            status = int(status)
            break
        else:
            print("Erro! Digite apenas 1 ou 0.")

    # -----------------------------------------
    # Contagem condicional:
    # Soma apenas as peças aprovadas (código 1)
    # e contabiliza defeituosas quando for 0.
    # -----------------------------------------

    if status == 1:
        aprovadas += 1
    else:
        defeituosas += 1

# Relatório final
print("\n========================================")
print(" RELATÓRIO FINAL DO LOTE ")
print("========================================")

print(f"Total de peças aprovadas: {aprovadas}")
print(f"Total de peças defeituosas: {defeituosas}")

# Verificação do lote
if defeituosas > 2:
    print("Status do lote: REJEITADO")
else:
    print("Status do lote: ACEITO")

print("\nSistema encerrado com sucesso.")