# gertrude.julia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto

#Cena 1
IMG = {
       'cena' : 'http://www.plantasdecasas.com/wp-content/uploads/2013/02/Casa-Salvador-304.jpg',
       'hand' : 'https://media-minecraftforum.cursecdn.com/attachments/133/64/635733362039447280.png',
       'umbrella' : 'https://d30y9cdsu7xlg0.cloudfront.net/png/678625-200.png'
       }

def mockCena():
  mCena = Cena(img=IMG['cena']);
  hand = Elemento(img=IMG['hand'], trt="Mãos", style=dict(top=200, left=125, height=100, width=70))
  umbrella = Elemento(img=IMG['umbrella'], trt="Guarda Chuva", style=dict(top=200, left=125, height=100, width=70))
  hand.entra(mCena)
  umbrella.entra(mCena)
  mCena.vai();
  
mockCena();