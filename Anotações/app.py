def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        # aqui ele faz a conversao para um numero inteiro

        try:
            valor = float(valor)
            return valor
        except ValueError:
            # aqui ele faz a conversao para um numero de ponto flutuante
            pass


while True:  # aqui esta o laço
    numero = converte_numero(input("Digite um numero: "))

    if numero is None:  # aqui ele verifica se o numero esta valido para o calculo
        print("Error: isso não e um numero")
    else:
        print(numero * 5)
