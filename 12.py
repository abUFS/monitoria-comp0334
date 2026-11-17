# Parte 1 - preencher cardapio
cardapio = {}

n = int(input())

for i in range(n):
    codigo = int(input())
    descricao = input()
    preco = float(input())

    cardapio[codigo] = {"descricao" : descricao, "preço" : preco}

# Parte 2 - calcular pedido
conta = 0

def calcular_pedido(codigo, qtd):
    if codigo in cardapio and qtd > 0:
        valor = cardapio[codigo]["preço"] * qtd
        return valor
    else:
        return 0
    
receber_pedidos = True
while receber_pedidos:

    codigo = int(input())

    if codigo == 0:
        receber_pedidos = False
    else:
        qtd = int(input())

        conta += calcular_pedido(codigo, qtd)

print(f"{conta:.2f}")
