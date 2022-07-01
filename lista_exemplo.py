l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]
        # aqui eu estou jogando todos os valores na variavel e criando uma nova lista

ex2 = [v * 2 for v in l1]
ex3 = [(v,v2) for v in l1 for v2 in range(3)]
        # para cada valor do l1 eu utilizo o segundo for jogando os valores na V2 que tem range de 3  

l2 = ['macaco1','macaco2','macaco3']
ex4 = [v.replace('a','@').upper() for v in l2]  
        # aqui o v ta repondo a letra a por @ na l2 

tupla = (
        ('chave','valor'),
        ('chave2','valor2')
)
ex5 = [(y,x) for x,y in tupla]
        # aqui esta trocando a ordem das palavras da tupla. ao inves de sair [('chave','valor')] - 
                # vai sair [('valor','chave')].
ex5 = dict(ex5)
        # aqui eu so estou transformando o ex5 em dicionario 


l3 = list(range(100))
        # uma humilde lista que vai de 0 ate 100
ex6 = [v for v in l3 if v % 2 == 0]
        # aqui ele vai exibir apenas os numeros divisiveis por 2 

ex7 = [v if v % 3 == 0 else 'Nao é' for v in l3]
        # ele verifica os numeros divisiveis por 3 e os que nao forem ele coloca 'nao é '

print(ex7)