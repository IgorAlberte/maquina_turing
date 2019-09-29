#Define uma transição
from classe_estado import Estado

class Transicao:
	
	def __init__(self, estado_inicial, estado_final):
		self.estado_inicial = estado_inicial
		self.estado_final = estado_final
		self.operacoes = []
	
	def add_operacao(self, operacao):
		self.operacoes.append(operacao)
	
	def get_estado_inicial(self):
		return Estado(self.estado_inicial)
		
	def get_estado_final(self):
		return Estado(self.estado_final)
	
	
