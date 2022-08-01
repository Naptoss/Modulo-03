from vendas.formata import preco


def aumento(valor, porcetagem, formata=False):
    r = valor + (valor * (porcetagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r


def reduz(valor, porcetagem, formata=False):
    r = valor - (valor * (porcetagem / 100))

    if formata:
        return preco.real(r)
    else:
        return r
