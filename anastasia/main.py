##############################################TAKE2############################################################
# Importando a biblioteca do Vitollino
from _spy.vitollino.main import *

# Configuracao da largura e altura da cena
STYLE["width"] = 1000
STYLE["height"] = "600px"

# Criando um dicionario com as imagens
IMG = {
	'background' : 'https://media-cdn.tripadvisor.com/media/photo-s/07/34/b1/37/parque-do-japao.jpg',
	'moeda_piscante' : 'http://3.bp.blogspot.com/-xxHdoS90xwo/VR1jjtJUh1I/AAAAAAAAQAI/1Sw0A7IliUw/s1600/Coin%2B4.gif',
	'moeda' : 'https://cdn.icon-icons.com/icons2/651/PNG/512/Icon_Business_Set_00003_A_icon-icons.com_59841.png',
	'seta' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png'
}

# Cria a classe da cena
class Lago:
	# Construindo a cena com os objetos e as funcoes de cada objeto
	def __init__(self):

		# Inicia o inventario
		INVENTARIO.inicia();
        
		# Cria a cena
		self.__lago = Cena(img = IMG['background']);
        
		# Cria os objetos da cena juntamente com suas funcoes
		self.__moedaPiscante = Elemento(img=IMG['moeda_piscante'], vai=self.__vaiMoedaPiscante, cena=self.__lago, trt="Guarda Chuva", style=dict(top=100, left=170, bottom=20, height=150, width=70))
		self.__moeda = Elemento(img=IMG['moeda'], vai=self.__vaiMoeda, cena=self.__lago, trt="Moeda Piscante", style=dict(top=150, left=220, bottom=20, height=150, width=70))
		seta = Elemento(img=IMG['seta'], cena=self.__lago, trt="Seguir em frente", style=dict(top=80, left=160, bottom=20, width=30))
        
	# Coloca a moeda piscante no inventario
	def __vaiMoedaPiscante(self, _=0): INVENTARIO.bota(self.__moedaPiscante)      

	# Coloca a moeda normal no inventario
	def __vaiMoeda(self, _=0): INVENTARIO.bota(self.__moeda)
		#self.__moeda.vai = vaiMoeda
		#self.__moeda.entra(self.__lago)

	# Executa a cena
	def vai(self): self.__lago.vai();