try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro de Name', erro)
except IndexError as erro:
    print('Error de Index ')
except Exception as erro:
    print('Error inesperado')
