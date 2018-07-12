# gertrude.anastasia.main.py
##############################################TAKE2############################################################

# Importando a biblioteca do Vitollino
from _spy.vitollino.main import *
from meredith.main import Aleia

# Configuracao da largura e altura da cena
STYLE["width"] = 1000
STYLE["height"] = "600px"

# Criando um dicionario com as imagens
IMG = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/digitalizar0003.png?disp=inline',
	'moeda_piscante' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_7_5942055903.png?disp=inline',
	'moeda' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_9_9462807394.png?disp=inline',
	'seta' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png'
}

# Cria a classe da cena
class Lago:
	# Construindo a cena com os objetos e as funcoes de cada objeto
	def __init__(self):
        
		# Cria a cena
		self.__lago = Cena(img = IMG['background']);
        
		# Cria os objetos da cena
		self.__moedaPiscante = Elemento(img=IMG['moeda_piscante'], style=dict(top=450, left=250, bottom=20, width=150));
		self.__moeda = Elemento(img=IMG['moeda'], style=dict(top=450, left=350, bottom=20, width=150));
		seta = Elemento(img=IMG['seta'], trt="Seguir em frente", style=dict(top=195, left=575, bottom=20, width=30));

		# Funcoes
		self.__moedaPiscante.vai = self.__vaiMoedaPiscante;
		self.__moeda.vai = self.__vaiMoeda;
		seta.vai = Aleai().vai;        
        
		# Adicionando a Cena
		self.__moedaPiscante.entra(self.__lago);
		self.__moeda.entra(self.__lago);
		seta.entra(self.__lago);

	# Coloca a moeda piscante no inventario
	def __vaiMoedaPiscante(self, _=0): INVENTARIO.bota(self.__moedaPiscante)      

	# Coloca a moeda normal no inventario
	def __vaiMoeda(self, _=0): INVENTARIO.bota(self.__moeda)

	# Executa a cena
	def vai(self, *_): self.__lago.vai()