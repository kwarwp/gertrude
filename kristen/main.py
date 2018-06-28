# gertrude.kristen.main.py
################################################TAKE1##########################################################

from _spy.vitollino.main import *
from anastasia.main import Lago
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background' : 'https://media-cdn.tripadvisor.com/media/photo-s/07/94/9a/9a/primeiro-portao-instalado.jpg',
	'mapa' : '',
	'pixacao' : 'https://i0.wp.com/www.heversonbarbosa.com/wp-content/uploads/2017/05/home-seta.png',
	'portao' : 'https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline'
}

class Entrada:

	def __init__(self):

		# Criando elementos
		self.__entrada = Cena(img = IMG['background']);
		portao = Elemento(img = IMG['portao'], style = dict(left=215, top=0, width= 575,bottom=0));
		pixacao = Elemento(img = IMG['pixacao'], style = dict(left=0, top=95, width= 100,bottom=20));
		aviso = Texto(self.__entrada, "O portao esta trancado");

		# Funcoes
		portao.vai = aviso.vai;
		pixacao.vai = Lago().vai;
        
		# Anexando elementos na cena
		portao.entra(self.__entrada);
		pixacao.entra(self.__entrada);

	def vai(self): self.__entrada.vai();

Entrada().vai();