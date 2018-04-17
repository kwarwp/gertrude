# gertrude.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto

#Cena 1
IMG = {
       'home' : 'http://kafgw.com/wp-content/uploads/inside-houses-canterbury-college-university-windsor_1337735.jpg',
       'hand' : 'https://media-minecraftforum.cursecdn.com/attachments/133/64/635733362039447280.png',
       'umbrella' : 'https://d30y9cdsu7xlg0.cloudfront.net/png/678625-200.png',
       'casaco' : 'https://www.achildsplace.org/wp-content/uploads/2014/10/rain-coat-clip-art-raincoat-300x247.png',
       'cellphone' : 'https://vignette.wikia.nocookie.net/uncyclopedia/images/6/6b/Cellphone.png/revision/latest?cb=20100105203250',
       'window' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/oie_transparent.png?disp=inline'
       }

def createCena1():
  cena1 = Cena(img=IMG['home']);
  umbrella = Elemento(img=IMG['umbrella'], trt="Guarda Chuva", style=dict(top=100, left=190, bottom=20, height=150, width=70))
  casaco = Elemento(img=IMG['casaco'], trt="Casaco", style=dict(top=150, left=20, bottom=20, height=150, width=70))
  phone = Elemento(img=IMG['cellphone'], trt="Telefone", style=dict(top=180, left=180, bottom=20, width=30))
  window = Elemento(img=IMG['window'], trt="Janela", style=dict(top=-15, left=60, bottom=10, width=200))
  hand = Elemento(img=IMG['hand'], trt="Mãos", style=dict(top=200, left=125, height=100, width=70))
  
  #txt = Texto(mCena, "Coé");
  umbrella.entra(cena1)
  casaco.entra(cena1)
  phone.entra(cena1)
  window.entra(cena1)
  hand.entra(cena1)
  #hand.direita = #cena2
  cena1.vai()
  
createCena1()