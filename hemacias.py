def paciente_por_extenso(sigla):
    if sigla == "H":
        return "Homem"
    if sigla == "M":
        return "Mulher"
    if sigla == "C":
        return "Crianca"
    if sigla == "I":
        return "Idoso"

def analisar_hemacias(valor, tipo_paciente):
    limite_inferior = [4.5, 4, 4.07, 3.9]
    limite_superior = [6.1, 5.4, 5.37, 5.36]
    tipos_pacientes = "HMCI"

    indice_tipo_paciente = tipos_pacientes.index(tipo_paciente)
    limt_inf = limite_inferior[indice_tipo_paciente]
    limt_sup = limite_superior[indice_tipo_paciente]

    if valor < limt_inf:
        return "Baixo"
    elif valor <= limt_sup:
        return "Normal"
    else:
        return "Alto"


parar = False

while not parar:
    entrada = input().split()

    if entrada == "*":
        parar = True
    else:
        valor = float(entrada[0])
        tipo_paciente = entrada[1]
        por_extenso = paciente_por_extenso(tipo_paciente)
        categorizacao = analisar_hemacias(valor, tipo_paciente)

        resultado = "Hemacias %.2f/mm3(%s) = %s" % (valor, por_extenso, categorizacao)
        
        resultado = "Hemacias {:.2f}/mm3({}) = {}".format(valor, por_extenso, categorizacao)

        resultado = f"Hemacias {valor: .2f}/mm3({por_extenso}) = {categorizacao}"
        

        print(resultado)
