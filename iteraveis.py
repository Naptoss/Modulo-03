# lists, tuples, str -> sequences -> iteravel

nome = 'Antonio Gabinio'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))


print('olha o for')

for letra in gerador:
    print(letra)

# try:
#     print(next(iterador))  # A
#     print(next(iterador))  # N
#     print(next(iterador))  # T
#     print(next(iterador))  # O
#     # print(next(iterador))  # N
#     # print(next(iterador))  # I
#     # print(next(iterador))  # O
# except:
#     pass
#     # aqui quando chegar ao final do interador ele vai suprimir o erro

# # se os iteradores da linha 10 a 12 nao estivessem comentados
# print('Cade os valores')
# for valor in iterador:             # o resultado sairia com o "Cade os valores como ultimo" em ultimo lugar
#     print(valor)

# for letra in nome:
#     print(letra)

# print('#'*80)

# for letra in nome:
#     print(letra)

# print(letra)
