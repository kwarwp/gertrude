# gertrude.julia.main.py
from _spy.vitollino.main import *
STYLE["width"] = 1000
STYLE["height"] = "600px"

#Take 2
IMG = {
       'background' : 'https://media-cdn.tripadvisor.com/media/photo-s/07/34/b1/37/parque-do-japao.jpg',
       'moeda_piscante' : 'http://3.bp.blogspot.com/-xxHdoS90xwo/VR1jjtJUh1I/AAAAAAAAQAI/1Sw0A7IliUw/s1600/Coin%2B4.gif',
       'moeda' : 'https://cdn.icon-icons.com/icons2/651/PNG/512/Icon_Business_Set_00003_A_icon-icons.com_59841.png',
       'seta' : 'http://ap.imagensbrasil.org/images/PNG-Setadourada.png'
       }

class Lago:
	def __init__(self):
		INVENTARIO.inicia();
		self.__lago = Cena(img = IMG['background']);
		moedaPiscante = Elemento(img=IMG['moeda_piscante'], cena=self.__lago, trt="Guarda Chuva", style=dict(top=100, left=170, bottom=20, height=150, width=70))
		moeda = Elemento(img=IMG['moeda'], cena=self.__lago, trt="Moeda Piscante", style=dict(top=150, left=220, bottom=20, height=150, width=70))
		seta = Elemento(img=IMG['seta'], cena=self.__lago, trt="Telefone", style=dict(top=80, left=160, bottom=20, width=30))
		moeda.vai = INVENTARIO.bota        
	def vai(self): self.__lago.vai();
    
l = Lago();
l.vai()
    