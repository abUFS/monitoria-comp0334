# Forma 1
def tipo_triangulo(a, b, c):
    return "EQUILATERO"

def obtem_lados(entrada):
    pass

for_para_receber = True #modelando a situação "Não é para parar"
while for_para_receber: # not True == False
    entrada = input()
    if entrada != "FIM":
        ladoA, ladoB, ladoC = obtem_lados(entrada)
        print(tipo_triangulo(ladoA,ladoB,ladoC))
    else:
        for_para_receber = False
