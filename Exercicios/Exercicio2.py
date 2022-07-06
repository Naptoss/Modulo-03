# def func1():
#     return "macaco"

# def func2(funcao):
#     return funcao()

# executando = func2(func1)
# print(executando)


##########################################

# Bem, dessa forma foi como eu fiz, para ajudar quem não entendeu. Eu coloquei os args e kwargs nas funções para usar com o get, ou seja, ela executa qnd achar aquela variavel. assim eu posso enviar todos os kwargs para todas as funções e elas executam as variaveis que acharem, mesmo que tenha mais kwargs do que ela va usar. Por exemplo,  no meu print eu enviei 2 kwargs e como podemos ver minha funcao1 utiliza apenas o kwargs = nome, caso eu nao utilize o 'nome = kwargs.get('nome')', utilize apenas a variavel de entra nome, meu algoritimo 'funcao1(nome)', vai apontar erro, dizendo que tem mais argumentos na entrada da função. Não sei se consegui explicar bem



# Mas do jeito que ta ai eu posso enviar todos os kwargs de uma vez e cada função pega o que quer.

# # def mestre(funcao): # Dessa forma acusa que naoo tem argumento posicional
# #     return funcao() # Porque nao da pra por la em baixo um argumento dentro da função que já é argumento
# # func(func(arg))
 
# def mestre(funcao, *arg, **kwargs): # dessa forma repassa pra função os *arg e *kwarg qnd existirem
#     return funcao(*arg, **kwargs)
 
 
# def funcao1(*args, **kwargs):
#     nome = kwargs.get('nome')
#     return f'OI {nome}'
 
 
# def funcao2(*args, **kwargs):
#     nome = kwargs.get('nome')
#     saudacao = kwargs.get('saudacao')
#     return f'{saudacao} {nome}'
 
 
# print(mestre(funcao2, nome='Antonio', saudacao='Ola'))