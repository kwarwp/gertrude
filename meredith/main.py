#######################################################TAKE3############################################################
# gertrude.anastasia.main.py
# Importando a biblioteca do Vitollino
from _spy.vitollino.main import *

# Configuracao da largura e altura da cena
STYLE["width"] = 1000
STYLE["height"] = "600px"

# Criando um dicionario com as imagens
IMG = {
	'background' : 'http://ebendinger.jbrj.gov.br/fotos/75.jpg',
	'passarinho' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/Bird2.png?disp=inline',
	'ninho' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_16_2807468112.png?disp=inline',
	'seta' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png'
}

# Cria a classe da cena
class Aleia:
	# Construindo a cena com os objetos e as funcoes de cada objeto
	def __init__(self):
        
		# Cria a cena
		self.__aleia = Cena(img = IMG['background']);
        
		# Cria os objetos da cena
		self.__passarinho = Elemento(img=IMG['passarinho'], style=dict(top=430, left=470, bottom=20, width=100));
		self.__ninho = Elemento(img=IMG['ninho'], style=dict(top=100, left=600, bottom=20, width=150));
		seta = Elemento(img=IMG['seta'], style=dict(top=350, left=380, bottom=20, width=30))        

		# Funcoes        
        
		# Adicionando a Cena
		self.__passarinho.entra(self.__aleia);
		self.__ninho.entra(self.__aleia);
		seta.entra(self.__aleia);

	# Executa a cena
	def vai(self, *_): self.__aleia.vai()

Aleia().vai()