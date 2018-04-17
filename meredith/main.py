# gertrude.meredith.main.py
from _spy.vitollino.main import Cena

linkIMG = "http://pre09.deviantart.net/3a5c/th/pre/f/2011/105/c/2/fractal_png_by_elevation_world-d3e2cex.png"

class Cena2():

  def __init__(self):
    self.cena2 = Cena(img = linkIMG)
    cena1 = Cena()
    cena1.vai = self.cena1Vai
    self.cena2.esquerda = cena1

  def vai(self, *_):    
    self.cena2.vai()
  def cena1Vai(self):
    from anastasia.main import Cena1
    Cena1().vai
  