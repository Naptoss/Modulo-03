#Obs: a partir do momento que e setado um valor padrao pro argumento(como no nome=None), 
# os proximos que vem depois dele tambem precisam de um padrao

# def func(a1,a2,a3,a4,a5, nome=None, a6):  <--- Forma errada
#     print(a1,a2,a3,a4,a5, a6) 
# func(1,2,3,4,5)   

# def func(a1,a2,a3,a4,a5, nome=None,a6=None): <--- Forma certa
#     print(a1,a2,a3,a4,a5, nome,a6)

# func(1,2,3,4,5) 
#Obs: como na func nao o nome e nem o a6, ele vai retornar none 2 vezes.

#==========================================================================================
#obs: logo abaixo temos um desempacotamento
# def func(*args):
#     print(args)

# lista = [1,2,3,4,5]
# func(*lista,10,20,30,40,50)    <---- aqui eu estou pedindo para desempacotar a lista, adicionando os dados na tupla

#==========================================================================================

# def func(*args):
#     print(args)

# lista1 = [1,2,3,4,5,6]    
# lista = [10,20,30,40,50]

# func(*lista1,*lista)      <----- Aqui eu fiz 2 desempacotamento e juntei as duas
                        
#==========================================================================================

# def func(*args, **kwargs):
#     print(args)

#     idade = kwargs.get("idade")

#     if idade is not None:
#         print(idade)
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista,*lista2,idade = 18)

#==========================================================================================

# def func(*args, **kwargs):
#     print(args)

#     idade = kwargs("idade") 

#     if idade is not None:
#         print(idade)
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista,*lista2) <---- se na linha 50 tiver idade, e aqui na linha 56 nao tiver isso vai gerar um erro.
