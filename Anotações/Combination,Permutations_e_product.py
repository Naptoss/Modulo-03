"""
Combinations - Permutations e Product - Itertools
Combinação - ordem não importa
Permutação - Ordem Importa 
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product


pessoa = ['Luiz', 'Antonio', 'Theo', 'Monkey', 'Angelo', 'Luke', 'Sammy']


for grupo in product(pessoa):
    print(grupo)
