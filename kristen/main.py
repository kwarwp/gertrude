# gertrude.kristen.main.py
################################################TAKE1##########################################################

from _spy.vitollino.main import *
from anastasia.main import Lago
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/35788257_1787410928014659_8815247365167382528_n.png?disp=inline',
	'mapa' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original.jpg?disp=inline',
	'muro' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/muro.png?disp=inline',
	'portao' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/portao.png?disp=inline'
}

class Entrada:

	def __init__(self):

		# Criando elementos
		self.__entrada = Cena(img = IMG['background']);
		portao = Elemento(img = IMG['portao'], style = dict(left=227, top=15, width= 505, height='500px' ,bottom=0));
		self.__mapa = Elemento(img = IMG['mapa'], style = dict(left=290, top=300, height='80px', width=60, bottom=0, border='3px solid brown'));
		muro = Elemento(img = IMG['muro'], style = dict(left=0, top=160, width= 240,bottom=20));
		aviso = Texto(self.__entrada, "O portao esta trancado");

		# Funcoes
		portao.vai = aviso.vai;
		self.__mapa.vai = self.__vaiMapa;
		muro.vai = Lago().vai;
        
		# Anexando elementos na cena
		portao.entra(self.__entrada);
		self.__mapa.entra(self.__entrada);
		muro.entra(self.__entrada);

	def __vaiMapa(self, _=0): INVENTARIO.bota(self.__mapa)

	def vai(self, *_): self.__entrada.vai();
    
Entrada().vai()