# gertrude.anastasia.main.py
from _spy.vitollino.main import Cena
from gertrude.meredith.main import Cena2

linkIMG = "https://openclipart.org/image/800px/svg_to_png/232279/MandelbrotFrame.png"

def Cena1():
  cena1 = Cena(img = linkIMG)
  cena2MOCK = Cena()
  cena1.direita = cena2MOCK
  cena2MOCK.vai = Cena2
  
  cena1.vai()
  
def Game():
  Cena1()

if __name__ == "__main__":
	Game()
	print(Cena2)