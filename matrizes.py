n = int(input())

matriz = []
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(0)

matriz[0][1] = 1
print(matriz[0][1])
print(matriz[1][1])

def criar_matriz_quadrada(n):
    return [[0 for _ in range(n)] for _ in range(n)]

matriz2 = criar_matriz_quadrada(n)

matriz2[0][0] = 1
print(matriz2[0][0])
print(matriz2[1][0])
