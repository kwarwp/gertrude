# gertrude.stacy.main.py
from _spy.vitollino.main import *

class Personagem:

	def __init__(self, nome = '', posicao = dict(top=100, left=20, bottom=20, height=150, width=70), fala = '', img = ''):
		if len(fala) == 0:
			texto = Texto(cena, fala);
			self.__personagem = Elemento(img = img, trt = nome, style = posicao, vai = texto.vai);
		else:
			self.__personagem = Elemento(img = img, trt = nome, style = posicao);
	
	def getPersonagem(self): return self.__personagem;

class Objeto:

	def __init__(self, nome, posicao = dict(top=100, left=20, bottom=20, height=150, width=70), pontuacao, acao, img):
		self.__objeto = Elemento(img = img, trt = nome, style = posicao, vai = acao);

	def getObjeto(self): return self.__objeto;

class Cena:

	def __init__(self, background, score, objetos = [], personagens = []):
		self.__cena = Cena(img = background);
		for p in personagens: p.getPersonagem().entra(self.__cena);
		for o in objetos : o.getObjeto().entra(self.__cena);

	def vai(self): self.__cena.vai();