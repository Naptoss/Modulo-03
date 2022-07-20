"""
count - intertools
"""

from itertools import count

contador = count()

for valor in contador:
    print(valor)

    if valor > 10000:
        break
