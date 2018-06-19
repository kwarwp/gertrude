# gertrude.kristen.main.py
from _spy.vitollino.main import *
from anastasia.main import Lago

################################################TAKE1##########################################################

STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background' : 'https://media-cdn.tripadvisor.com/media/photo-s/07/94/9a/9a/primeiro-portao-instalado.jpg',
	'pixacao' : 'https://interartive.org/wp-content/uploads/pixo1.jpg',
	'portao' : 'https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline'
}

class Entrada:

	def __init__(self):

		self.__entrada = Cena(img = IMG['background']);
		aviso = Texto(self.__entrada, "O portao esta trancado");
		portao = Elemento(img = IMG['portao'], cena=self.__entrada, vai=aviso.vai, style = dict(left= 215, top=0,height= '600px', width= 575,bottom=0))
		pixacao = Elemento(img = IMG['pixacao'], cena=self.__entrada, vai=Lago().vai, style = dict(left=0, top=95,height= '505px', width= 250,bottom=20));

	def vai(self): self.__entrada.vai();

Entrada().vai();