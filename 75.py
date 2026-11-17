
# Preencher o dicionário de voos
voos = {}

for i in range(37):
    entrada = input().split()

    voo = int(entrada[0])
    vagas = int(entrada[1])

    voos[voo] = vagas

# Marcar os voos, quando disponível
def fazer_reserva(rg, voo):
    if voo in voos:
        if voos[voo] > 0:
            print(rg)
            voos[voo] -= 1
        else:
            print("INDISPONIVEL")
    else:
        print("INDISPONIVEL")

encerrar = False # encerrar a marcação de voos
while not encerrar:
    entrada = input()

    if entrada == "9999":
        encerrar = True
    else:
        entrada = entrada.split() # 9999
        rg = entrada[0]
        voo = int(entrada[1])

        fazer_reserva(rg, voo)
