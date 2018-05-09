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
TRANSPARENTE = "http://1.bp.blogspot.com/-eK24sreQNsg/Uvy1AT5iVSI/AAAAAAAAAGo/TRHh_nkqhVY/s1600/fundo-blog.png"
FLORESTA = "https://st.depositphotos.com/1718692/2958/i/950/depositphotos_29580473-stock-photo-stones-and-tree-roots-in.jpg"
OCULOS = "https://www.dvosky.com/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/d/v/dvsk1003-preto-prata.png"
class Estados:
    def __init__(self):
        floresta = Cena(FLORESTA)
        self.fantasma = Cena()
        floresta.vai()
        self.galhos = gag = Elemento(img=TRANSPARENTE,tit="galhos", style=dict(
            left=28, top=130, width=60, height="60px"))
        gag.entra(floresta)
        gag.vai = self.fogo_galhos
        self.pedra = aqua = Elemento(img=TRANSPARENTE,tit="pedras", style=dict(
            left=500, top=300, width=60, height="60px")) 
        aqua.entra(floresta)
        aqua.vai = self.fogo_pedra
        self.oculos = ocu = Elemento(img=OCULOS, tit="OCULOS", style=dict(
            left=28, top=130, width=60, height="60px"))
        inv.bota(self.oculos)
        ocu.vai = self.fogo_oculos
        
    def fogo_pedra(self, *_):
        input("Voce fez fogo usando pedras! Como vocÃÂª fez?")
        self.pedra.entra(self.fantasma)
    def fogo_galhos(self, *_):
        input("voce fez fogo usando galhos! como vc fez?")
        self.galhos.entra(self.fantasma)
    def fogo_oculos(self, *_):
        input("voce fez fogo usando oculos! como vc fez?")
        self.oculos.entra(self.fantasma)
        
        

        
        
if __name__ == "__main__":
    Estados()
        

