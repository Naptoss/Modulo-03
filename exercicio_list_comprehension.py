
string = '0123456789012345678901234567890123456789'
n = 10
comp = [(i, i + n) for i in range(0,len(string), n)]
        #aqui eu estou fazendo uma tupla com 2 valores, o 