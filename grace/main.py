# gertrude.grace.main.py
from _spy.vitollino.main import Cena, Elemento

linkIMG = "http://pre09.deviantart.net/3a5c/th/pre/f/2011/105/c/2/fractal_png_by_elevation_world-d3e2cex.png"

class Cena2():
  def __init__(self):
    linkOlho = "http://icons.iconarchive.com/icons/custom-icon-design/mono-general-4/512/eye-icon.png"

    self.cena = Cena(img = linkIMG)
    olho = Elemento(img = linkOlho, style = dict(top = '10', left = '10'))

  def vai(self, *_):
    self.cena.vai()    
  def connectEsquerda(self, cena):
    self.cena.esquerda = cena
  def connectDireita(self, cena):
    self.cena.direita = cena
    
