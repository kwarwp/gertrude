#######################################################TAKE3############################################################
# gertrude.meredith.main.py
# Importando a biblioteca do Vitollino
from _spy.vitollino.main import *
from danae.main import Guarita

# Configuracao da largura e altura da cena
STYLE["width"] = 1000
STYLE["height"] = "600px"

# Criando um dicionario com as imagens
IMG = {
	'aleia1' : 'http://ebendinger.jbrj.gov.br/fotos/75.jpg',
	'aleia2' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',    
	'aleia3' : 'http://ebendinger.jbrj.gov.br/fotos/75.jpg',    
	'passarinho' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/Bird2.png?disp=inline',
	'ninho' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_16_2807468112.png?disp=inline',
	'macaco': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/srmacaco2.png?disp=inline',    
	'seta' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png'
}

# Cria a classe da cena
class Aleia:
	# Construindo a cena com os objetos e as funcoes de cada objeto
	def __init__(self):
        
		# Cria a cena
		self.__aleia = Cena(img = IMG['aleia1']);
        
		# Cria os objetos da cena
		self.__passarinho = Elemento(img=IMG['passarinho'], style=dict(top=430, left=470, bottom=20, width=100));
		self.__ninho = Elemento(img=IMG['ninho'], style=dict(top=100, left=600, bottom=20, width=150));
		seta = Elemento(img=IMG['seta'], style=dict(top=350, left=380, bottom=20, width=30))        

		# Funcoes    
		seta.vai = Aleia2().vai;
        
		# Adicionando a Cena
		self.__passarinho.entra(self.__aleia);
		self.__ninho.entra(self.__aleia);
		seta.entra(self.__aleia);

	# Executa a cena
	def vai(self, *_): self.__aleia.vai()

class Aleia2:

	def __init__(self):
         
		# Criando elementos
		self.__aleia2 = Cena(img = IMG['aleia2']);
        
		Texto(self.__aleia2, "Leticia: Ai!!! Acho que machuquei minha perna. Vou precisar de algo para poder continuar nossa aventura").vai();        

		# Funcoes
        
		# Anexando elementos na cena

	def vai(self, *_): self.__aleia2.vai();
    
class Aleia3:

	def __init__(self):
         
		# Criando elementos
		self.__aleia3 = Cena(img = IMG['aleia3']);
		macaco = Elemento(img=IMG['macaco'], style=dict(top=300, left=300, bottom=20, width=150));

		# Funcoes
		macaco.vai = Texto(self.__aleia3, 'Se eu fosse voces eu seguiria em frente atÃ© a guarita, lÃ¡ voces vao poder se alimentar e recuperar o folego').vai;
        
		# Anexando elementos na cena
		macaco.entra(self.__aleia3);

	def vai(self, *_): self.__aleia3.vai();

# Aleia().vai()
# Aleia2().vai()
Aleia3().vai()