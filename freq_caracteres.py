# Solução comentada:
# Questão 2835 - Contando frequência de caracteres
# Link: https://www.thehuxley.com/problem/2835

# Estratégia
# Dividir o problema em 2 partes:
# 1 - Criar um dicionário com caracteres e frequências
# 2 - Imprimir na ordem alfabética inversa
 
linha = input() # Entrada do usuário. Uma string (sequência de caracteres)

caracteres_freq = {} # Cria um dicionário vazio. Outra alternativa: caracteres_freq = dict()

# Um dicionário armazena pares de chaves (keys) e valores (values) -> {key1:value1, key2:value2, ...}.
# Quem serão nossas chaves e valores?
# Para esse exemplo, nossas chaves serão os caracteres e os valores serão as frequencias dos caracteres
# ex: Se `entrada` for "mamma mia!", então nosso dicionário `caracteres_freq` será:
# {'m': 4, 'a': 3, ' ': 1, 'i': 1, '!': 1}
# Obs: Veja que o espaço ' ' também é um caractere.

# Iterar sobre todos os caracateres na linha
for caractere in linha:
    if caractere in caracteres_freq.keys(): # Se o caractere for encontrado nas chaves (keys()) do dicionário
        caracteres_freq[caractere] += 1 # Então, devemos incrementar a frequência (valor) dessa chave em 1
    else: # Caso contrário, ou seja, o caractere não está entre as chaves do dicionário
        caracteres_freq[caractere] = 1 # Então, adicionamos ao dicionário com a frequência 1.

# Agora temos um dicionario `caracteres_freq` com os caracteres e suas frequências
# Vamos então imprimir 

# Criar uma lista das chaves
lista_de_chaves = list(caracteres_freq.keys())
# Ordenar em ordem alfabética inversa (reverse=True)
chaves_invertidas = sorted(lista_de_chaves, reverse=True)

# Imprimir as chaves e os valores
for chave in chaves_invertidas:
    valor = caracteres_freq[chave]
    print(chave, valor)