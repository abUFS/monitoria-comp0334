T = int(input())
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def contar_buracos(palavra):
    tamanho = len(palavra)
    indice = 0
    buracos = 0
    while indice < tamanho:
        letra = palavra[indice].upper()

        if letra == "A" or letra == "D"  ... letra == "R":
            buracos += 1
        if letra == "B":
            buracos += 2

        indice += 1
    return buracos

def contar_buracos_com_for(palavra):
    buracos = 0
    tamanho = len(palavra)
    for i in range(tamanho):
        letra = palavra[i]
        if letra ==  "A" or letra == "D" or letra == "O" or letra == "P" or letra == "Q" or letra == "R":
            buracos += 1
        if letra == "B":
            buracos += 2
    return buracos

for i in range(T): # range == intervalo [0, T[
    palavra = input()
    buracos = contar_buracos(palavra)
    print(buracos)



    
while n <= m:
    if m % 2 != 0:
        print(m)
        break
    if n != 0:
        continue
    m = m - 1
            