################################################TAKE4##########################################################

from _spy.vitollino.main import *
#from anastasia.main import Lago
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'background1' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',
	'background2' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',    
	'cabine': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/guarita.png?disp=inline',
	'maquina_biscoito': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/maquinadebolachakk2.png?disp=inline',
	'lanterna': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_26_3323460880.png?disp=inline'    
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
        
		self.__lanterna = Elemento(img=IMG['lanterna'], style=dict(top=0,bottom=20, width=230, left=57));
		self.__maquinaBiscoito = Elemento(img=IMG['maquina_biscoito'], style=dict(top=0,bottom=20, width=230, left=57));

		# Funcoes
		self.__lanterna.vai = self.__pegarLanterna;
        
		# Anexando elementos na cena
		self.__lanterna.entra(self.__guarita2);
		self.__maquinaBiscoito.entra(self.__guarita2);
        
	def __pegarLanterna(self, _=0):
		INVENTARIO.bota(self.__lanterna);
    
def vai(self, *_): self.__guarita2.vai();

# Guarita1().vai();
# Guarita2().vai();