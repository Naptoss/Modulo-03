from vendas.calcula_preco import aumento, reduz
from vendas.formata import preco


preco = 49.90
preco_com_aumento = aumento(valor=preco, porcetagem=15, formata=True)
print(preco_com_aumento)


preco = 49.90
preco_com_reducao = reduz(valor=preco, porcetagem=15, formata=True)
print(preco_com_reducao)
