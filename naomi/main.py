# gertrude.naomi.main.py
from _spy.vitollino.main import *

#Imagens do jogo
IMG = {     
       'mario' : 'http://www.imagenspng.com.br/wp-content/uploads/2015/02/super-mario-mario-04.png',
       'sonic' : 'https://vignette.wikia.nocookie.net/epic-rap-battles-of-cartoons/images/d/d0/Sonic.png/revision/latest?cb=20170804133442',
       'backgroundMario' : 'http://www.misucell.com/data/out/12/IMG_544236.png',
       'backgroundSonic' : 'https://orig00.deviantart.net/5c2c/f/2016/068/3/f/green_hill_zone_background_1_by_sonicmechaomega999-d9uisrx.png',
       'background' : 'https://vignette.wikia.nocookie.net/sonic-the-hedgehog-fan/images/f/f7/Awesome_Background.png/revision/latest?cb=20151026172243'
       }
       
class Cena1:

	def __init__(self, personagem):
		self.__cena1 = Cena(img = IMG['background']);
		mario = Elemento(img=IMG['mario'], cena=self.__cena1, trt="Mario", style=dict(top=100, left=20, bottom=20, height=150, width=70))
		sonic = Elemento(img=IMG['sonic'], cena=self.__cena1, trt="Sonic", style=dict(top=100, left=200, bottom=20, height=150, width=70))
		#if personagem == 'Mario': mario.vai = Cena(img = IMG['backgroundMario'], esquerda = Cena1('Sonic')).vai;
		#elif personagem == 'Sonic': sonic.vai = Cena(img = IMG['backgroundSonic'], esquerda = Cena1('Mario')).vai;
		def trade():
			personagem = False;
			print(personagem)            
		mario.vai = trade            
        
	def vai(self): self.__cena1.vai();
c = Cena1('Mario');
c.vai();