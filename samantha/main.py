from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv

from soraya.main import Bloco
from browser import alert


STYLE["width"] = 600
STYLE["height"] = "600px"

#############################################TAKE0#######################################################

BACKG1 = "http://galvaoweb.com.br/escolas_01/wp-content/uploads/2017/02/01-patio.jpg"
P1N = "https://vignette.wikia.nocookie.net/phineasferb/images/4/40/Perry_-_Imagem_Promocional_%2826%29.png"
P2 = "https://vignette.wikia.nocookie.net/phineasferb/images/4/40/Perry_-_Imagem_Promocional_%2826%29.png"
P3 = "https://vignette.wikia.nocookie.net/phineasferb/images/4/40/Perry_-_Imagem_Promocional_%2826%29.png"

def Take0():
    backgr =Cena(img=BACKG1)
    narrador=  Elemento (img=P1N, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
    personagem1 =  Elemento (img=P2, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
    personagem2 =  Elemento (img=P3, style=dict (left=95, top= 100, height=100, width=100, bottom=15))
    narrador.personagem1.personagem2.entra(backgr)
    
    Take.vai()