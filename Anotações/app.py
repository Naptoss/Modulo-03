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

    if numero is not None:  # aqui ele verifica se o numero e valido, se for ele multiplica por 5
        print(numero*5)
    else:
        print("Isso nao e um numero")
