# Parte 1 - preencher cardapio
cardapio = {}

n = int(input())

for i in range(n):
    codigo = int(input())
    descricao = input()
    preco = float(input())

    cardapio[codigo] = {"descricao" : descricao, "preço" : preco} # [descricao, preco]

# Parte 2 - calcular pedido
receber_pedidos = True #
conta = 0
while receber_pedidos:
    codigo = int(input())

    if codigo == 0:
        receber_pedidos = False
    else:
        qtd = int(input())

        if codigo in cardapio and qtd > 0:
            valor = cardapio[codigo]["preço"] * qtd
            conta += valor
        
        # valor = cardapio.get(codigo, {"preço" : 0})["preço"] * qtd
        # conta += valor

print(f"{conta:.2f}")
