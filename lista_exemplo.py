l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
        # aqui eu estou jogando todos os valores na variavel e criando uma nova lista

ex2 = [v * 2 for v in l1]
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
        # para cada valor do l1 eu utilizo o segundo for jogando os valores na V2 que tem range de 3  

l2 = ['antonio','sammy','allyson']
ex4 = [v.replace('a','@') for v in l2]  
        # aqui o v ta repondo a letra a por @ na l2 

print(ex4)