def func(arg, arg2):
    return arg * arg2


func(5, 5)


def a(x, y): return x * y


print(a(3, 2))


#################################

lista = [
    ['P1', 5],
    ['P2', 54],
    ['P3', 12],
    ['P4', 10],
    ['P5', 19],
    ['P6', 11],
    ['P7', 23],
]


def func(item):
    return item[1]


lista.sort(key=func)
print(lista)

# Aqui o codigo se resume a funcoes que foram criadas para poder ordernar a lista do menor para o maior
# sem expressoes anonimas.
# Criados fuction e parametros para poder fazer o codigo funcionar

###################################

lista = [
    ['P1', 5],
    ['P2', 54],
    ['P3', 12],
    ['P4', 10],
    ['P5', 19],
    ['P6', 11],
    ['P7', 23],
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

# Aqui foi se usado a expressao anonima, ou seja economizando linha e deixando o codigo mais arrumado
# O codigo esta pegando o maior numero para o menor.
