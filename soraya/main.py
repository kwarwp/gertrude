# gertrude.soraya.main.py
########################################################CENAMAPA####################################################
from _spy.vitollino.main import Cena, STYLE
from _spy.vitollino.main import INVENTARIO as inv
from _spy.vitollino.main import *

STYLE['width'] = 700
STYLE["height"] = "600px"

TRANSPARENTE = "http://1.bp.blogspot.com/-eK24sreQNsg/Uvy1AT5iVSI/AAAAAAAAAGo/TRHh_nkqhVY/s1600/fundo-blog.png"
MAPA0 = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original.jpg"
MAPA1 = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original11.jpg"
MAPA2 = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/original4.jpg"
#MAPA3 = " "
#MAPA4 = " "

########################################################################################################################

def Mapa0(): 

    back0 = Cena(img=MAPA0)
    back0.vai()
    
Mapa0()

########################################################################################################################

def Mapa1():
  
    back0 = Cena(img=MAPA1)
    back0.vai()
    self.local = loc = Elemento(img=TRANSPARENTE,tit="lago das tartarugas", style=dict(
            left=28, top=130, width=60, height="60px"))
    loc.entra(MAPA0)
    loc.vai = self.take2
    def take2(self, *_):
        cena_lago()
    
Mapa1()

##########################################################################################################################

def Mapa2():

    back0 = Cena(img=MAPA2)
    back0.vai()
    self.local = locc = Elemento(img=TRANSPARENTE,tit="lago das tartarugas", style=dict(
            left=28, top=130, width=60, height="60px"))
    locc.entra(MAPA0)
    locc.vai = self.take2
    def take2(self, *_):
        cena_lago()
    
Mapa2()