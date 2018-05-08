# gertrude.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from sara.main import *

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

class Cena1:
	def __init__(self):
  		self.__cena1 = Cena(img=IMG['home']);
  		cena2 = Cena2();
  		self.__umbrella = Elemento(img=IMG['umbrella'], trt="Guarda Chuva", style=dict(top=100, left=170, bottom=20, height=150, width=70))
  		self.__casaco = Elemento(img=IMG['casaco'], trt="Casaco", style=dict(top=150, left=220, bottom=20, height=150, width=70))
  		self.__phone = Elemento(img=IMG['cellphone'], trt="Telefone", style=dict(top=180, left=180, bottom=20, width=30))
  		self.__window = Elemento(img=IMG['window'], trt="Janela", style=dict(top=-15, left=60, bottom=10, width=200))
  		self.__lampada = Elemento(img=IMG['lampada'], trt="Lampada", style=dict(top=0, left=130, bottom=10, width=50))
  		self.__personagem = Elemento(img=IMG['personagem'], trt="personagem", style=dict(top=100,left=70,bottom=0, width=120))
  		self.__bola = Elemento(img=IMG['bola'], trt="bola", style=dict(top=220, left=0, bottom=10, width=70))
        #txt = Texto(mCena, "CoÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ©"
  		self.__oculos = Elemento(img=IMG['oculos'], trt="Oculos", style=dict(top=160, left=20,bottom=20, width=50))
  		self.__umbrella.entra(self.__cena1)
  		self.__casaco.entra(self.__cena1)
  		self.__phone.entra(self.__cena1)
  		self.__window.entra(self.__cena1)
  		self.__personagem.entra(self.__cena1)
  		self.__lampada.entra(self.__cena1)
  		self.__bola.entra(self.__cena1)
  		self.__oculos.entra(self.__cena1)
  		self.__personagem.vai = self.teste
  		self.__cena1.direita = cena2;
	def vai(self): self.__cena1.vai();
	def teste(self): print('Foi');
    
c = Cena1();
c.vai();