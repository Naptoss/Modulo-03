# primeiro foi criado o nome do arquivo, e o "w+" foi usado para escrever no arquivo
file = open('abc.txt', 'w+')
file.write("Linha 1\n")
file.write("Linha 2\n")
file.write("Linha 3\n")
# 3 linhas que foram escritas no arquivo

file.seek(0, 0)
# posição global do arquivo, ou seja ele comeca do inicio e vai ate o final do arquivo

print("###########")

print("Lendo linhas: ")

print()

print(file.read())  # aqui esta lendo o arquivo

print()

print("###########")

print()

file.seek(0, 0)  # aqui ele volta pro inicio do arquivo
print(file.readline(), end='')  # aqui o cursor esta no final da linha 1
print(file.readline(), end='')  # aqui o cursor ele continua da onde ele parou
print(file.readline(), end='')

print()

print("###########")

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()
# aqui fechou o arquivo
