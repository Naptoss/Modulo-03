"""
def - definir um parametro 
não repetir o codigo varias vezes 
"""


def saudacao(msg="Ola", nome="usuário"):
    nome = nome.replace('e','3')
    msg = msg.replace('3','e')
    return f'{msg} {nome}'
        # Aqui ele so troca no nome o e por 3 e o mesmo sentindo se aplica no msg

variavel = saudacao()

print(variavel)
