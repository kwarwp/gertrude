################################################TAKE4##########################################################

from _spy.vitollino.main import *
#from anastasia.main import Lago
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background1' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',
	'background2' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',    
	'cabine': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/guarita.png?disp=inline',
	'mapa' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original.jpg?disp=inline',
	'pixacao' : 'https://i0.wp.com/www.heversonbarbosa.com/wp-content/uploads/2017/05/home-seta.png',
	'portao' : 'https://activufrj.nce.ufrj.br/file/pedropeclat/1528988110963.png?disp=inline'
}

class Guarita1:

	def __init__(self):

		# Criando elementos
		self.__guarita = Cena(img = IMG['background1']);
		cabine = Elemento(img=IMG['cabine'], style=dict(top=0,bottom=20, width=230, left=57));

		# Funcoes
		cabine.vai = Guarita2();
        
		# Anexando elementos na cena
		cabine.entra(self.__guarita);

	def vai(self, *_): self.__guarita.vai();

class Guarita2:

	def __init__(self):

		# Criando elementos
		self.__guarita2 = Cena(img = IMG['background2']);
		cabine = Elemento(img=IMG['cabine'], style=dict(top=0,bottom=20, width=230, left=57));

		# Funcoes
        
		# Anexando elementos na cena
		cabine.entra(self.__guarita);
    
def vai(self, *_): self.__guarita2.vai();

# Guarita().vai();
# Guarita2().vai();