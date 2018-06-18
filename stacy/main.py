# gertrude.stacy.main.py
from _spy.vitollino.main import *

class Personagem:

	def __init__(self, nome = '', cena = '', posicao = dict(top=100, left=20, bottom=20, height=150, width=70), fala = '', img = ''):
		if len(fala) == 0:
			texto = Texto(cena, fala);
			self.__personagem = Elemento(img = img, cena = cena, trt = nome, style = posicao, vai = texto.vai);
		else:
			self.__personagem = Elemento(img = img, cena = cena, trt = nome, style = posicao);
	
	def getPersonagem(self): return self.__personagem;
      