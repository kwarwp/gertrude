# gertrude.grace.main.py
from _spy.vitollino.main import Cena

linkIMG = "http://pre09.deviantart.net/3a5c/th/pre/f/2011/105/c/2/fractal_png_by_elevation_world-d3e2cex.png"
class Cena2():
  def __init__(self):
    self.cena = Cena(img = linkIMG)
    self.cenaEsquerda = Cena()
    self.cenaDireita = Cena()
    self.cena.direita = self.cenaDireita
    self.cena.esquerda = self.cenaEsquerda

  def vai(self, *_):
    self.cena.vai()    
  def connectEsquerda(self, cena):
    self.cenaEsquerda.vai = cena.vai
  def connectDireita(self, cena):
    self.cenaDireita.vai = cena.vai
