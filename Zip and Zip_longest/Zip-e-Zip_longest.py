"""
Zip - Unindo iteráveis 
Zip_longest - Itertools
"""

from itertools import zip_longest


cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA', ]

cidades_estados = zip(estados, cidades)
# Nesse zip ele ta pegando apenas os 3 respectivas cidades e estados
# a saida disso sera a junção dos 3 iteraveis e deixando Monte Belo e o Outro sem
# junção com os outros estados
print(list(cidades_estados))


# cidades_estados2 = zip_longest(cidades, estados)
# No zip_longest aqui faz a mesma coisa que o zip, entretanto, quando chega
# em Monte Belo e o Outro ele usa o None no [1] para repor a ausencia de uma
# outro Estado
