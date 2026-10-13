def bissexto(ano):
    if ano % 4 == 0:
        return 1
    else:
        return 0

def contagem_dias(dia, mes, ano):
    if mes == 1:
        return dia
    elif mes == 2:
        return dia + 31
    elif mes == 3:
        return dia + 59 + bissexto(ano)
    elif mes == 4:
        return dia + 90 + bissexto(ano)
    

print(contagem_dias(15,3,4))