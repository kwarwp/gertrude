################################################TAKE4##########################################################

from _spy.vitollino.main import *
from grace.main import Guarita
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',
	'mapa' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original.jpg?disp=inline',
	'pixacao' : 'https://i0.wp.com/www.heversonbarbosa.com/wp-content/uploads/2017/05/home-seta.png',
	'portao' : 'https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline'
}

class Aleia2:

	def __init__(self):

		Texto() 
         
		# Criando elementos
		self.__guarita = Cena(img = IMG['background']);

		# Funcoes
        
		# Anexando elementos na cena

	def vai(self, *_): self.__guarita.vai();
    
# Guarita().vai()