#Representa uma máquina de Turing
class Maquina:
	
	def __init__(self):
		self.simbolos = []
		self.fitas = []
		self.estados = []
		self.transicoes = []
		
	#adiciona um símbolo aos símbolos da máquina
	def add_simbolo(self, simbolo):
		self.simbolos.append(simbolo)
		
	def add_fita(self, fita):
		self.fitas.append(fita)
	
	def add_estado(self, estado):
		self.estados.append(estado)
		
	def add_transicoes(self, transicao):
		self.transicoes.append(transicao)
		
