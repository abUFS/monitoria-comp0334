# Conta quantos "buracos" existem em uma palavra. Definido como a soma
# dos buracos de cada letra que compoe a palavra.
# "ADOPQR" letras com "1 buraco"
# "B" letras com "2 buracos"
# demais letras não contém buracos 

palavra = "ABACAXI"

# Usando o while para contabilizar
def contar_buracos_com_while(palavra):
    tamanho = len(palavra)
    indice = 0
    buracos = 0
    while indice < tamanho:
        letra = palavra[indice].upper()
        if letra in "ADOPQR":
            buracos += 1
        if letra in "B":
            buracos += 2
        indice += 1
    return buracos

# Usando for para contabilizar
def contar_buracos_com_for(palavra):
    buracos = 0
    for letra in palavra:
        if letra.upper() in "ADOPQR":
            buracos += 1
        if letra.upper() in "B":
            buracos += 2
    return buracos

# Usando .count()
def contar_buracos_com_count(palavra):
    buracos = 2*palavra.count("B")
    for letra in "ADOPQR":
        buracos += palavra.count(letra)
    return buracos

print(contar_buracos_com_while(palavra))
print(contar_buracos_com_for(palavra))
print(contar_buracos_com_count(palavra))