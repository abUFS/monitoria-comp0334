# Entrada: N número positivos. Receber até que seja informado um negativo
negativo = False # representa se o usuário informou um valor negativo

quantidade = 0 # quantidade de valores informados pelo usuário
soma = 0   # soma dos valores informados

while not negativo: # enquanto NÃO negativo. negativo = False, not negativo = True
    valor = int(input())  # Ex: 5

    if valor < 0: # Atualizar a variável da condição
        negativo = True
    else:
        soma = soma + valor   # soma = 0 + 5 = 5
        print("Soma parcial", soma)
        quantidade = quantidade + 1 # quantidade = 0 + 1 = 1
        print("Quantidade parcial", quantidade)

media = soma / quantidade

print(media)