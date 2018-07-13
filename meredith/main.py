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
	'aleia1': 'http://ebendinger.jbrj.gov.br/fotos/75.jpg',
	'aleia2': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/36410919_1803508649738220_8839554797003603968_n.png?disp=inline',    
	'aleia3': 'http://ebendinger.jbrj.gov.br/fotos/75.jpg',    
	'passarinho': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/Bird2.png?disp=inline',
	'ninho': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_16_2807468112.png?disp=inline',
	'maca': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_34_5062328837.png?disp=inline',    
	'pedra': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_22_9073509179.png?disp=inline',
	'bengala': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_5_5251419741.png?disp=inline',    
	'darwin': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/darwinghost_2.png?disp=inline',
	'macaco': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/srmacaco2.png?disp=inline',    
	'seta' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png'
}

SOUNDS = {
	'darwin': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/330860__andre-onate__indra-call.wav?disp=inline'
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
		self.__passarinho.vai = self.__saiPassarinho      
		seta.vai = Aleia2().vai;
        
		# Adicionando a Cena
		self.__passarinho.entra(self.__aleia);
		self.__ninho.entra(self.__aleia);
		seta.entra(self.__aleia);

	# Coloca o passarinho no ninho    
	def __saiPassarinho(self, _=0): 
		self.__passarinho.elt.style = dict(display= 'none');
		self.__ninho.elt.style = dict(display= 'none');
		ninho = Elemento(img=IMG['seta'], cena=self.__aleia, style=dict(top=100, left=600, bottom=20, width=150));
		maca = Elemento(img=IMG['maca'], style=dict(top=100, left=600, bottom=20, width=150));
		Texto(self.__aleia, 'Obrigado por colocar meu filho de volta no ninho como recompensa toma aqui essa fruta').vai()
		INVENTARIO.bota(maca)        

	# Executa a cena
	def vai(self, *_): self.__aleia.vai()

class Aleia2:

	def __init__(self):
         
		# Criando elementos
		self.__aleia2 = Cena(img = IMG['aleia2']);
                
		self.__pedra = Elemento(img=IMG['pedra'], style=dict(left=520, width=800, top=250, bottom=20));      
		self.__bengala = Elemento(img=IMG['bengala'], style=dict(left=670, top=270, bottom=20, width=500));        

		# Funcoes
		self.__bengala.vai = self.__pegarBengala;        
		self.__aleia2.esquerda = Aleia3();        
        
		# Anexando elementos na cena        
		self.__pedra.entra(self.__aleia2);
		self.__bengala.entra(self.__aleia2);        
		Texto(self.__aleia2, "Leticia: Ai!!! Acho que machuquei minha perna. Vou precisar de algo para poder continuar nossa aventura").vai();        

	def __pegarBengala(self, _=0):
		self.__bengala.elt.style = dict(display= 'none');
		Musica(sound=SOUNDS['darwin'], loop=False);
		Elemento(img=IMG['darwin'], cena=self.__aleia2, style=dict(left=700));          
		Texto(self.__aleia2, 'Devolvam minha bengala|||').vai();
        
	def vai(self, *_): self.__aleia2.vai();
    
class Aleia3:

	def __init__(self):
         
		# Criando elementos
		self.__aleia3 = Cena(img = IMG['aleia3']);
		macaco = Elemento(img=IMG['macaco'], style=dict(top=300, left=300, bottom=20, width=150));
		seta = Elemento(img=IMG['seta']);

		# Funcoes
		macaco.vai = Texto(self.__aleia3, 'Se eu fosse voces eu seguiria em frente ate voces vao poder se alimentar e recuperar o folego').vai;
		seta.vai = Guarita().vai;        
        
		# Anexando elementos na cena
		macaco.entra(self.__aleia3);
		seta.entra(self.__aleia3);

	def vai(self, *_): self.__aleia3.vai();

# Aleia().vai()
# Aleia2().vai()
# Aleia3().vai()