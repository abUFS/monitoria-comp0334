def ContaDigitosPares(valor):
    if valor < 0:
        return ContaDigitosPares((-1)*valor)
    if valor < 10:
        return 1 if valor % 2 == 0 else 0
    else:
        return (1 if (valor % 10) % 2 == 0 else 0) + ContaDigitosPares(valor // 10) 



valor = int(input())

qtd_digitos_pares = ContaDigitosPares(valor)

print(qtd_digitos_pares)