from _spy.vitollino.main import Cena, STYLE, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv
from kristen.main import Entrada
STYLE['width'] = 700
STYLE["height"] = "600px"

PATIO= "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/20180710_111303.jpg?disp=inline"
LEKES= "http://3.bp.blogspot.com/-_JxmohXYIHI/Ud89A7TrTHI/AAAAAAAABQY/RGp-9STuc2c/s1600/pooh7.png"
NANA = "https://vignette.wikia.nocookie.net/monica4438/images/5/59/Magali.png/revision/latest?cb=20161221230552&path-prefix=es"
LETICIA = "http://www.imagenspng.com.br/wp-content/uploads/2015/06/monica-02.png"

def cena3():

    fundo1 = Cena(img=PATIO, direita=Entrada().vai)
    lekes = Elemento(img=LEKES, style = dict(top = 50,right = 500, height = '250px' , width = 200))
    nana = Elemento(img=NANA, style = dict(top = 300,left = 510, height = '250px' , width = 180))
    leticia = Elemento(img=LETICIA, style = dict(top = 300,left = 400, height = '250px' , width = 200))
    
    lekes.entra(fundo1)
    leticia.entra(fundo1)
    nana.entra(fundo1)
    fundo1.vai()
    
    amgs = Texto(fundo1 ,"AndrÃ©- Cara, vocÃª ouviu que o Jardim BotÃ¢nico estÃ¡ em manutenÃ§Ã£o?    Matheus- Sim, fiquei sabendo que coisas estranhas vem acontecendo lÃ¡!")
    leticiatxt = Texto(fundo1,"LetÃ­cia- Miga, vocÃª viu que tem algo acontecendo no Jardim? Vamos lÃ¡ ver?")
    nanatxt = Texto(fundo1,"Nana- Mas vocÃª Ã© curiosa ein, e eu tambÃ©mâ¦ Vamos!")

    lekes.vai=amgs.vai
    nana.vai=nanatxt.vai
    leticia.vai=leticiatxt.vai
    
cena3()