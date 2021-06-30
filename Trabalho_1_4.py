def DefinirDia(indice):
    x = indice - 11519

    codigoDia = int(x / 96)

    if codigoDia == 0:
        return "Domingo"

    if codigoDia == 1:
        return "Segunda"

    if codigoDia == 2:
        return "Terça"

    if codigoDia == 3:
        return "Quarta"

    if codigoDia == 4:
        return "Quinta"

    if codigoDia == 5:
        return "Sexta"

    if codigoDia == 6:
        return "Sábado"

def DefinirHora(indice):
    x = indice - 11519

    HoraMin = ((x/96)-int(x/96))*96*15

    Hora = int(HoraMin/60)
    Min = round(HoraMin % 60)

    return  str(Hora) + ':' + str(Min)

def DataHora(indice):

    return  str(DefinirDia(indice)) + ' ' + str(DefinirHora(indice))
