carrinho = []

carrinho.append(('Produto 1', 20))
carrinho.append(("Produto 2", 30))
carrinho.append(("Produto 3", 50))
carrinho.append(("Produto 4", 60))

print(carrinho)
# aqui ele ira exibir os 4 produtos em seguencia seus valores determinados

compra = sum([(p[1]) for p in carrinho])
print(compra)


"""
FUNÇÃO SUM() EM PYTHON
A soma dos números na lista é necessária em todos os lugares. 
Python fornece uma função embutida sum() que resume os números da lista.

"""

# -----> pegar o preço do carrinho e somar para dar o resultado total


# """
# NAO FAZER DAS SEGUINTES MANEIRAS: <----

# total = 0
# for produto in carrinho:
#     total = produto[1]
# print(total)

# """
