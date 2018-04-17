# gertrude.anastasia.main.py
from _spy.vitollino.main import Cena

linkIMG = "https://openclipart.org/image/800px/svg_to_png/232279/MandelbrotFrame.png"

class Cena1():
  def __init__(self):
    from meredith.main import Cena2
    self.cena1 = Cena(img = linkIMG)
    cena2 = Cena2()
    cena1.direita = cena2

    cena1.vai()
  def vai(self, *_):
    self.cena1.vai()

def Game():
  cena1 = Cena1()
  cena1.vai()

if __name__ == "__main__":
	Game()
