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
TRANSPARENTE = "https://png.pngtree.com/element_origin_min_pic/16/07/08/16577f6b0279750.jpg"
FLORESTA = "https://st.depositphotos.com/1718692/2958/i/950/depositphotos_29580473-stock-photo-stones-and-tree-roots-in.jpg"

class Estados:
    def __init__(self):
        floresta = Cena(FLORESTA)
        self.fantasma = Cena()
        floresta.vai()
        galhos = Elemento(img=TRANSPARENTE,tit="galhos", style=dict(
            left=28, top=130, width=60, height="60px"))
        galhos.entra(floresta)
        self.pedra = aqua = Elemento(img=TRANSPARENTE,tit="pedras", style=dict(
            left=500, top=300, width=60, height="60px")) 
        aqua.entra(floresta)
        
        aqua.vai = self.fogo_pedra
    def fogo_pedra(self, *_):
        input("Voce fez fogo usando pedras! Como vocÃª fez?")
        self.pedra.entra(self.fantasma)
        

        
        
if __name__ == "__main__":
    Estados()
        

