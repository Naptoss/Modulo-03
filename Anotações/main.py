try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro de Name', erro)
    # Ao retornar o erro de NameError, ele retorna o que esta no print

except IndexError as erro:
    print('Error de Index ')
    # Ao dar Erro de Index ele retorna no console a mensagem personalizada para
    # o erro especifico.

except Exception as erro:
    print('Error inesperado')
