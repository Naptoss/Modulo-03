numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

novos_numeros = [numero for numero in numeros if numero > 5]
# um filter nessa linha a qual pega somente os numeros maiores de 5

impares = [numero for numero in numeros if numero % 2 != 0]
# outro filter a qual ele pega somente os numeros impares

pares = [numero for numero in numeros if numero % 2 == 0 or numero * 2 == 0]
# outro filter so que com numeros pares

outro_if = []

print(numeros)
print(novos_numeros)
print(impares)
print(pares)
