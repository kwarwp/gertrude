# gertrude.meredith.main.py
from _spy.vitollino.main import Cena
from anastasia.main import Cena1

linkIMG = "http://pre09.deviantart.net/3a5c/th/pre/f/2011/105/c/2/fractal_png_by_elevation_world-d3e2cex.png"

def Cena2():
  cena2 = Cena(img = linkIMG)
  cena1MOCK = Cena()
  cena2.esquerda = cena1MOCK
  cena1MOCK.vai = Cena1
  
  cena2.vai()