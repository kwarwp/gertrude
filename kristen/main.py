# gertrude.kristen.main.py
################################################TAKE1##########################################################
from _spy.vitollino.main import *
from anastasia.main import Lago
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background' : 'https://media-cdn.tripadvisor.com/media/photo-s/07/94/9a/9a/primeiro-portao-instalado.jpg',
	'pixacao' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png',
	'portao' : 'https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline'
}

class Entrada:

	def __init__(self):

		self.__entrada = Cena(img = IMG['background']);
		aviso = Texto(self.__entrada, "O portao esta trancado");
		portao = Elemento(img = IMG['portao'], cena=self.__entrada, vai=aviso.vai, style = dict(left= 215, top=0,height= '600px', width= 575,bottom=0))
		pixacao = Elemento(img = IMG['pixacao'], cena=self.__entrada, vai=Lago().vai, style = dict(left=0, top=95, width= 100,bottom=20));

	def vai(self): self.__entrada.vai();

Entrada().vai();