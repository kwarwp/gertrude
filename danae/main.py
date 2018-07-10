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
         
		# Criando elementos
		self.__aleia2 = Cena(img = IMG['background']);
        
		Texto(self.__aleia2, "Letícia: Ai!!! Acho que machuquei minha perna. Vou precisar de algo para poder continuar nossa aventura").vai();        

		# Funcoes
        
		# Anexando elementos na cena

	def vai(self, *_): self.__aleia2.vai();
    
Aleia2().vai()