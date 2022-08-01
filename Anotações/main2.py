# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise
#         # esse raise ta interando o try ali de baixo juntamente com o except


# try:
#     print(divide(2, 0))
# except:
#     print('Erro de divisao')


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 nao pode ser 0")
    return n1 / n2


try:
    print(divide(2, 0))
except ValueError as error:
    print(error)
