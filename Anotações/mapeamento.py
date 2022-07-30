from dados import produtos, pessoas, lista

precos = list(map(lambda p: p['preco'], produtos[0]))

for preco in precos:
    print(preco)
