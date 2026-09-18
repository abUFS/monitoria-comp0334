# 1 - entrada
tipo = input() # tipo da media
a = int(input()) # valor 1
b = int(input()) # valor 2
c = int(input()) # valor 3

# 2 - processamento
if tipo == "A":
    media = (a + b + c) / 3
elif tipo == "H":
    media = 3 / (1/a + 1/b + 1/c)
elif tipo == "G":
    media = (a*b*c)**(1/3)

# 3 - saída/resultado
print("%.3f" % media) # f float
