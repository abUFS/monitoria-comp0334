def contar_buracos(palavra):
    buracos = 0

    for letra in palavra:
        if letra in "ADOPQR":
            buracos = buracos + 1
        if letra == "B":
            buracos = buracos + 2

    return buracos

n = int(input())

for i in range(n):
    palavra = input()
    buracos = contar_buracos(palavra)
    print(buracos)