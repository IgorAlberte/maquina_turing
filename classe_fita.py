class Fita:
	
	def __init__(self, tipo):
		self.tipo = tipo
		self.posicao_atual = 0
		self.conteudo = []
	
	def mudar_posicao(self, direcao):
		if direcao == 'D':#anda para a direita
			self.posicao_atual = self.posicao_atual+1
			#tratar questão de fita acabar
			
		elif direcao == 'E':#anda para a esquerda
			self.posicao_atual = self.posicao_atual-1
			#tratar questão de fita acabar para a esquerda
			
		elif direcao == 'I':#imóvel
			self.posicao_Atual = self.posicao_atual
	
	#muda conteúdo da célula atual para conteudo_novo
	def mudar_conteudo(self, conteudo_novo):
		self.conteudo[self.posicao_atual] = conteudo_novo
	
	#devolve conteúdo da célula atual
	def conteudo_atual(self):
		return self.conteudo[self.posicao_atual]
