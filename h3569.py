""""
Escreva um programa em que o usuário entre com 
dois ângulos internos de um triângulo e o programa 
calcule o 3o ângulo do triângulo.

Formato de entrada:
Ângulo 1 (valor inteiro)
Ângulo 2 (valor inteiro)

Formato de saída:
Ângulo 3 (valor decimal com 6 casas decimais)

Adaptada do problema 3569 no the huxley
Fonte: https://www.thehuxley.com/problem/3569?locale=pt_BR
"""

primeiro_angulo_entrada = input()
primeiro_angulo = int(primeiro_angulo_entrada)

segundo_angulo_entrada = input()
segundo_angulo = int(segundo_angulo_entrada)

""" 
OBS: podemos realizar a entrada e conversão para float
em apenas uma linha.
Ex:
valor = int(input())
""" 

# Soma dos angulos internos do traingulo é 180º
terceiro_angulo = 180 - primeiro_angulo - segundo_angulo

# Para os alunos que precisam usar o print no estilo C
print("3o angulo=%.6f" %terceiro_angulo)

# Para os alunos que já aprenderam f-strings, podem usar o print abaixo:
print(f"3o angulo={terceiro_angulo:.6f}")
