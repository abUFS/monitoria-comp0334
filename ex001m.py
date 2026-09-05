"""
Faça um programa que calcule a multiplicação de dois números inteiros.

Entrada: dois número inteiros. Um por linha.
Saída: A multiplicação dos dois número. Ver formato do exemplo.

# exemplo entrada:
> 6
> 3

# exemplo de saída:
> 6 x 3 = 18
"""

# 
# dados/entrada -> processamento -> exibir/saída(s)

# dados/entrada
primeiro = int(input())
segundo  = int(input())

# processamento
multiplicacao = primeiro * segundo

# exibir/saída(s):

# No Python existem várias formas de obter o mesmo resultado.
# Abaixo temos 3 alternativas para imprimir a resposta no formato esperado.
# Verifiquem com professor da disciplina quais serão aceitas.

# Alternativa 1: usando a vírgula para separar os elementos a serem impressos
# É a opção mais simples, porém limitada e é fácil cometer erros ao escrever.
print(primeiro, "x", segundo, "=", multiplicacao)

# Alternativa 2: usando o estilo C, com %
# Com essa opção temos mais recursos, como por exemplo a formatação
print("%i x %i = %i" % (primeiro, segundo, multiplicacao))

# Alternativa 3: usando f-strings
# É o método atual para imprimir strings formatadas no Python.
print(f"{primeiro} x {segundo} = {multiplicacao}")
