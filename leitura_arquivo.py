#Leitura do arquivo de processamento e montagem da maquina
from classe_maquina import Maquina
from classe_estado import Estado
from classe_operacao import Operacao
from classe_transicao import Transicao
from classe_fita import Fita

def leitura_arquivo():
	nome = input("Digite o nome do arquivo com extensão: ")
	
	try:
		f = open(nome, "r") #coloca arquivo em f
	except FileNotFoundError:
		print("Não foi possível abrir o arquivo " + nome)
		return 
		
	maq = Maquina()
	qtd_transicoes = 0
	qtd_fitas = 0
	
			
	for k in f: #read line by line
		linha = k.split()
		
		if(len(linha) == 0):
			continue
		
		if linha[0] == "SIMB":
			for i in linha[1:len(linha)]:#primeira posição até fim da linha
				maq.add_simbolo(i)
		
		elif linha[0] == "FITAS":
			qtd_fitas = linha[1]#qtd fitas
			maq.set_qtd_fitas(int(qtd_fitas))
			
			for i in linha[2:len(linha)]:#primeira posição até fim da linha
				tipo = str(i)
				fita = Fita(tipo)
				maq.add_fita(fita)
				
		
		elif linha[0] == "ESTADOS":
			q = linha[1]
			maq.set_qtd_estados(int(q))
			
			for i in range(int(q)):
				estado = Estado(i, False)
				maq.add_estado(estado)
			
		elif linha[0] == "FINAIS":
			
			for i in linha[1:len(linha)]:
				maq.estados[int(i)].est_final = True
					
		elif linha[0] == "TRANSICOES":
			qtd_transicoes = int(linha[1])		
			break
	
	contador = 0
	for k in f: #lê transições
								
		l = k.split()
				
		if(contador >= qtd_transicoes):
			break
		
		estado_inicial = l[0]
		estado_final = l[1]
		
		posicao_estado_inicial = int(estado_inicial[1:])
		posicao_estado_final = int(estado_final[1:])
		
		transicao = Transicao(\
			maq.get_estados()[posicao_estado_inicial], \
			maq.get_estados()[posicao_estado_final])
		
		for i in range(maq.get_qtd_fitas()):
			#a partir do 3º elemento da linha
			#primeiro = estado_ini; segundo = estado_fim
			token = l[2+i]
			op = Operacao(token[0],token[1],\
				token[2])
			transicao.add_operacao(op)
			
		maq.add_transicao(transicao)
		
		contador = contador + 1#conta transições lidas
		
	
	return maq
			
		

maq = leitura_arquivo()
maq.le_fitas_entrada()
