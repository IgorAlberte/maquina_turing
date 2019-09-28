#Leitura do arquivo de processamento e montagem da máquina

nome = input("Digite o nome do arquivo com extensão: ")
f = open(nome, "r") #coloca arquivo em f

for i in f.readline():
	print i

