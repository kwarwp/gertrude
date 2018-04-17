# gertrude.danae.main.py
from _spy.vitollino.main import Cena

linkIMG = "https://openclipart.org/image/800px/svg_to_png/232279/MandelbrotFrame.png"

class Cena1():
  def __init__(self):
    self.cena = Cena(img = linkIMG)
    cenaEsquerda = Cena()
    cenaDireita = Cena()
    self.cena.direita = cenaDireita
    self.cena.esquerda = cenaEsquerda

  def vai(self, *_):
    self.cena.vai() 
  def conectEsquerda(self, cena):
    self.cena.esquerda = cena
  def connectDireita(self, cena):
    self.cena.direita = cena