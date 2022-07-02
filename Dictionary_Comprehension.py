# l1 = [1,2,3,4,5,6]
# l2 = [p*2 for p in l1]
# print(l2)


lista = [
    ('chave', 'valor'),
    ('chave2','valor2')
]

d1 = {y: x for x, y in lista}
print(d1)