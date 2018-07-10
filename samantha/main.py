# gertrude.samantha.main.py
################################################TAKE0##########################################################

from _spy.vitollino.main import *
from kristen.main import Entrada
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'start' : 'https://i0.wp.com/www.heversonbarbosa.com/wp-content/uploads/2017/05/home-seta.png'
}

SOUNDS = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/Bia.mp3?disp=inline'
}

class Menu:

	def __init__(self):

		# Criando elementos
		self.__menu = Cena();
		start = Elemento(img = IMG['start'], style = dict(left=500, top=300, width= 100,bottom=20));
		Musica(sound = SOUNDS['background']);

		# Funcoes
		start.vai = Entrada().vai;
        
		# Anexando elementos na cena
		start.entra(self.__menu);

	def vai(self): self.__menu.vai();

Menu().vai();