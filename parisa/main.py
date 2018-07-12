from _spy.vitollino.main import Cena, STYLE, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

STYLE['width'] = 700
STYLE["height"] = "600px"

PATIO= "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/20180710_111303.jpg?disp=inline"
LEKES= "http://3.bp.blogspot.com/-_JxmohXYIHI/Ud89A7TrTHI/AAAAAAAABQY/RGp-9STuc2c/s1600/pooh7.png"

def cena3():

    fundo1 = Cena(img=PATIO)
    lekes = Elemento(img=LEKES, style = dict(top = 50,right = 500, height = '250px' , width = 200))

    lekes.entra(fundo1)
    fundo1.vai()
    amgs = Texto(fundo1 ,"André- Cara, você ouviu que o Jardim Botânico está em manutenção?    Matheus- Sim, fiquei sabendo que coisas estranhas vem acontecendo lá!")
    lekes.vai=amgs.vai
    
cena3()