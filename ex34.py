positivos = 0

nao_zero = True

while nao_zero: # not False = True
    numero = int(input())
    if numero > 0:
        positivos += 1
    if numero == 0:
        nao_zero = False

print(positivos)