#Define uma transição
class Transicao:
	
	def __init__(self, estado_inicial, estado_final):
		self.operacoes = []
	
	def add_operacao(self, operacao):
		self.operacoes.append(operacao)