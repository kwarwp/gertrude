# gertrude.courtney.main.py
from _spy.vitollino.main import Cena, Texto, Elemento, STYLE
from _spy.vitollino.main import INVENTARIO as inv
from soraya.main import Bloco
STYLE["width"] = 600
STYLE["height"] = "600px"

TEMPLO = "http://3.bp.blogspot.com/-UsnGAupu3XM/VHvU2M5BHUI/AAAAAAAAdCE/UKbq_5dTM7k/s1600/IMG_6098.JPG"
CORREDOR = "http://i.muyinteresante.com.mx/dam/sociedad/historia/17/03/8/rabbit-hole-700-year-old-secret-knights-templar-cave-network-8-58c006f4a30df__880.jpg.imgo.jpg"
OCEANO = "https://freeclipartspot.com//storage/upload/ocean-clip-art/ocean-clip-art-51.jpg"
ALGA = "https://i.pinimg.com/originals/70/68/5f/70685fa634c3bb82a8eb5771a0a869ed.png"
CONCHA = "http://www.mat.uc.pt/~picado/conchas/imagens/p10.png"
AQUARIO = "https://www.tenstickers.pt/autocolantes-decorativos/img/preview/autocolante-decorativo-infantil-peixe-aquario-3634.png"
FLORESTA = "http://meioambiente.culturamix.com/blog/wp-content/gallery/futuro-das-florestas-do-mundo-1/Futuro-das-Florestas-do-Mundo-3.jpg"
class Estados:
    def __init__(self):
        floresta = Cena(FLORESTA)
        self.fantasma = Cena()
        floresta.vai()
        alga = Elemento(img=ALGA,tit="alga",style=dict(
            left=100, top=160, width=60, height="60px"))
        alga.entra(floresta)
        concha = Elemento(img=CONCHA,tit="concha",style=dict(
            left=200, top=160, width=60, height="60px"))
        concha.entra(floresta)
        self.peixe = aqua = Elemento(img=AQUARIO,tit="peixe",style=dict(
            left=300, top=160, width=60, height="60px"))
        aqua.entra(floresta)
        aqua.vai = self.fogo_peixe
    def fogo_peixe(self, *_):
        input("Voce fez fogo usando um peixe! Como vocÃª fez?")
        self.peixe.entra(self.fantasma)
        

        
        
if __name__ == "__main__":
    Estados()
        

