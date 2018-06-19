from _spy.vitollino.main import *
from anastasia.main import *

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

		entrada = Cena(img = IMG['background']);
		aviso = Texto(entrada, "O portao esta trancado");
		pixacao = Elemento(img = IMG['pixacao'], cena=entrada, vai=Lago().vai, style = dict(left=0, top=95,height= '505px', width= 250,bottom=20));
		portao = Elemento(img = IMG['portao'], cena=entrada, vai=aviso.vai, style = dict(left= 215, top=0,height= '600px', width= 575,bottom=0))
		entrada.vai();

Entrada();