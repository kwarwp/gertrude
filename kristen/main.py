# gertrude.kristen.main.py
################################################TAKE1##########################################################

from _spy.vitollino.main import *
from anastasia.main import Lago
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/digitalizar0001.jpg?disp=inline',
	'mapa' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original.jpg?disp=inline',
	'pixacao' : 'https://i0.wp.com/www.heversonbarbosa.com/wp-content/uploads/2017/05/home-seta.png',
	'portao' : 'https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline'
}

SOUNDS = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/330860__andre-onate__indra-call.wav?disp=inline'
}

class Entrada:

	def __init__(self):

		# Criando elementos
		self.__entrada = Cena(img = IMG['background']);
		portao = Elemento(img = IMG['portao'], style = dict(left=215, top=0, width= 575,bottom=0));
		self.__mapa = Elemento(img = IMG['mapa'], style = dict(left=240, top=300, height='80px', width=60, bottom=0, border='3px solid brown'));
		pixacao = Elemento(img = IMG['pixacao'], style = dict(left=0, top=95, width= 100,bottom=20));
		aviso = Texto(self.__entrada, "O portao esta trancado");
		Musica(sound = SOUNDS['background']);

		# Funcoes
		portao.vai = aviso.vai;
		self.__mapa.vai = self.__vaiMapa;
		pixacao.vai = Lago().vai;
        
		# Anexando elementos na cena
		portao.entra(self.__entrada);
		self.__mapa.entra(self.__entrada);
		pixacao.entra(self.__entrada);

	def __vaiMapa(self, _=0): INVENTARIO.bota(self.__mapa)

	def vai(self, *_): self.__entrada.vai();