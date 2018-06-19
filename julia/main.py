# gertrude.julia.main.py
from _spy.vitollino.main import *

#Take 2
IMG = {
       'background' : 'https://media-cdn.tripadvisor.com/media/photo-s/07/34/b1/37/parque-do-japao.jpg',
       'moeda_piscante' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_2_9367638513.png?disp=inline',
       'moeda' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_3_9501450609.png?disp=inline',
       'seta' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/cena1_capachuva.png?disp=inline'
       }

class Lago:
	def __init__(self):
		self.__lago = Cena(img = IMG['background']);
		moedaPiscante = Elemento(img=IMG['moeda_piscante'], cena=self.__lago, trt="Guarda Chuva", style=dict(top=100, left=170, bottom=20, height=150, width=70))
		moeda = Elemento(img=IMG['moeda'], cena=self.__lago, trt="Casaco", style=dict(top=150, left=220, bottom=20, height=150, width=70))
		seta = Elemento(img=IMG['seta'], cena=self.__lago, trt="Telefone", style=dict(top=180, left=180, bottom=20, width=30))
        
	def vai(self): self.__lago.vai();
    
l = Lago();
l.vai()
    