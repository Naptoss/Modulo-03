import sys
import time

def gera():
    r = [] # aqui cria uma array em branco
    for n in range(100): 
        r.append(n)
        time.sleep(0.1) # Aqui ele toma um sleep de 0,1
    return r
    # e na interação com o range ele pega de 0 a 99 colocando no array em branco

g = gera()

for v in g: 
    print(v)