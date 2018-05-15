# gertrude.julia.main.py
from _spy.vitollino.main import *
from sara.main import Cena2

#Cena 1
IMG = {
       'home' : 'http://kafgw.com/wp-content/uploads/inside-houses-canterbury-college-university-windsor_1337735.jpg',
       'personagem' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_2_9367638513.png?disp=inline',
       'umbrella' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_3_9501450609.png?disp=inline',
       'casaco' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/cena1_capachuva.png?disp=inline',
       'cellphone' : 'https://vignette.wikia.nocookie.net/uncyclopedia/images/6/6b/Cellphone.png/revision/latest?cb=20100105203250',
       'window' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/oie_transparent.png?disp=inline',
       'lampada' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_7202278580.png?disp=inline',
       'oculos': 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_9286555293.png?disp=inline',
       'bola' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_2_9661334197.png?disp=inline'
       
       }

class Cena1():
	def __init__():
  		self.__cena1 = Cena(img = IMG['home']);
  		umbrella = Elemento(img=IMG['umbrella'], cena=self.__cena1, vai=Cena2(True).vai, trt="Guarda Chuva", style=dict(top=100, left=170, bottom=20, height=150, width=70))
  		casaco = Elemento(img=IMG['casaco'], cena=self.__cena1, vai=Cena2(True).vai, trt="Casaco", style=dict(top=150, left=220, bottom=20, height=150, width=70))
  		phone = Elemento(img=IMG['cellphone'], cena=self.__cena1, vai=Cena2(False).vai, trt="Telefone", style=dict(top=180, left=180, bottom=20, width=30))
  		window = Elemento(img=IMG['window'], cena=self.__cena1, vai=Cena2(False).vai, trt="Janela", style=dict(top=-15, left=60, bottom=10, width=200))
  		lampada = Elemento(img=IMG['lampada'], cena=self.__cena1, vai=Cena2(False).vai, trt="Lampada", style=dict(top=0, left=130, bottom=10, width=50))
  		personagem = Elemento(img=IMG['personagem'], cena=self.__cena1, trt="personagem", style=dict(top=100,left=70,bottom=0, width=120))
  		bola = Elemento(img=IMG['bola'], cena=self.__cena1, trt="bola", vai=Cena2(False).vai, style=dict(top=220, left=0, bottom=10, width=70))
  		oculos = Elemento(img=IMG['oculos'], cena=self.__cena1, vai=Cena2(False).vai, trt="Oculos", style=dict(top=160, left=20,bottom=20, width=50))
		texto = Texto(self.__cena1,'Voce deve escolher entre os objetos da direita e os da esquerda');
		texto.vai()
        
	def vai(self): self.__cena1.vai();
    
    
    