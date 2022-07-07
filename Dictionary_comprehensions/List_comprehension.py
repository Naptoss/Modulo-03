
def multiplicacaoFN(x, y):
    return x * y


def somaFn(x, y):
    return x + y


def divisaoFn(x, y):
    return x / y


def subtracaoFn(x, y):
    return x - y
    # areá do hardcode onde se foi preciso digitar muito sem necessidade


numeros = [1, 2, 3, 4, 5]
divisao = [divisaoFn(numero, 2) for numero in numeros]
multiplicacao = [multiplicacaoFN(numero, 2) for numero in numeros]
subtracao = [subtracaoFn(numero, 2) for numero in numeros]
# continuidade do hardcode, onde ele faz a mesma função da list comprehension so que de uma forma mais bruta e sem necessidade

# numeros = [1, 2, 3, 4, 5]
# divisao = [numero / 2 for numero in numeros]
# multiplicacao = [numero * 2 for numero in numeros]
# subtracao = [numero - 2 for numero in numeros]
# Aqui e o basico de list comprehension, onde o codigo esta resumido tranquilamente

print(numeros)
print(divisao)
print(multiplicacao)
print(subtracao)
# Area dos retornos
