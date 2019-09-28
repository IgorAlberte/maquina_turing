#Classe que define a operação em uma fita para uma transição
class Operacao:
	
	def __init__(self, caractere_atual, caractere_novo, direcao):
		self.caractere_atual = caractere_atual
		self.caractere_novo = caractere_novo
		self.direcao = direcao
		
