# gertrude.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
from sara.main import *

#Cena 1
IMG = {
       'home' : 'http://kafgw.com/wp-content/uploads/inside-houses-canterbury-college-university-windsor_1337735.jpg',
       'hand' : 'https://media-minecraftforum.cursecdn.com/attachments/133/64/635733362039447280.png',
       'umbrella' : 'https://d30y9cdsu7xlg0.cloudfront.net/png/678625-200.png',
       'casaco' : 'https://www.achildsplace.org/wp-content/uploads/2014/10/rain-coat-clip-art-raincoat-300x247.png',
       'cellphone' : 'https://vignette.wikia.nocookie.net/uncyclopedia/images/6/6b/Cellphone.png/revision/latest?cb=20100105203250',
       'window' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/oie_transparent.png?disp=inline'
       }

class Cena1:
	def __init__(self):
  		self.__cena1 = Cena(img=IMG['home']);
  		cena2 = Cena2;
  		self.__umbrella = Elemento(img=IMG['umbrella'], trt="Guarda Chuva", style=dict(top=100, left=190, bottom=20, height=150, width=70))
  		self.__casaco = Elemento(img=IMG['casaco'], trt="Casaco", style=dict(top=150, left=20, bottom=20, height=150, width=70))
  		self.__phone = Elemento(img=IMG['cellphone'], trt="Telefone", style=dict(top=180, left=180, bottom=20, width=30))
  		self.__window = Elemento(img=IMG['window'], trt="Janela", style=dict(top=-15, left=60, bottom=10, width=200))
  		self.__hand = Elemento(img=IMG['hand'], trt="MÃÂÃÂÃÂÃÂ£os", style=dict(top=200, left=125, height=100, width=70))
  		#txt = Texto(mCena, "CoÃÂÃÂÃÂÃÂ©"
  		self.__umbrella.entra(self.__cena1)
  		self.__casaco.entra(self.__cena1)
  		self.__phone.entra(self.__cena1)
  		self.__window.entra(self.__cena1)
  		self.__hand.entra(self.__cena1)
  		self.__hand.vai = self.teste
  		self.__cena1.direita = cena2;
	def vai(self): self.__cena1.vai();
	def teste(self): print('Foi');
    
c = Cena1();
c.vai();