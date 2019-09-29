#Representa uma máquina de Turing
from classe_estado import Estado
from classe_fita import Fita
from classe_transicao import Transicao

class Maquina:
	
	def __init__(self):
		self.simbolos = []
		self.fitas = []
		self.estados = []
		self.qtd_estados = 0
		self.qtd_fitas = 0
		self.transicoes = []
		
	#adiciona um símbolo aos símbolos da máquina
	def add_simbolo(self, simbolo):
		self.simbolos.append(simbolo)
		
	def add_fita(self, fita):
		self.fitas.append(fita)
	
	def add_estado(self, estado):
		self.estados.append(estado)
				
	def add_transicao(self, transicao):
		self.transicoes.append(transicao)
		
	def set_qtd_estados(self, qtd):
		self.qtd_estados = qtd
			
	def get_estados(self):
		return self.estados
		
	def get_qtd_estados(self):
		return self.qtd_estados
		
	def set_qtd_fitas(self, qtd_fitas):
		self.qtd_fitas = qtd_fitas
	
	def get_qtd_fitas(self):
		return int(self.qtd_fitas)
		
	def get_fitas(self):
		return self.fitas
	
	def get_simbolos(self):
		return self.simbolos
	
	def to_string(self):
		print("SIMBOLOS:")
		print(self.simbolos)
		
		print("FITAS:")
		for i in self.fitas:
			print(i.tipo, ";", i.conteudo)
		
		print("QTD ESTADOS")
		print(self.qtd_estados)
		
		print("ESTADOS:")
		for e in self.estados:
			print(e.numero)
		
		print("TRANSICOES")
		for i in self.transicoes:
			print(i)
	
	#Lê conteúdo de cada fita do tipo 'in'
	def le_fitas_entrada(self):
		
		for f in self.get_fitas():
			
			if f.get_tipo() == "in":
				print("Símbolos possíveis: ", self.get_simbolos())
				string = input("Informe o conteúdo da fita separado por espaço: ")
				tokens = string.split()
				for i in tokens:
					f.add_caractere(i)
				f.add_caractere("-")#termina com '-'
				
		
		
				
		
