# 1 - Entrada: dados
tipo_media = input() # "A", "H" ou "G" string
a = int(input())
b = int(input())
c = int(input())

# 2 - Processamento : oque fazer com os dados (cálculos, decisões, etc) 

if tipo_media == "A":
    media = (a + b + c) / 3
elif tipo_media == "H": #SENÃO, SE
    media = 3 / (1/a + 1/b + 1/c)
elif tipo_media == "G": #SENÃO, SE
    media = (a*b*c)**(1/3)

# 3 - Saída: O que é o resultado e como exibir (variáveis, formatação, texto auxiliar)
print("%.3f" % media) # %i inteiro, %f float
