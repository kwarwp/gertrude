# gertrude.adda.main.py

from danae.main import Cena1
from grace.main import Cena2

cena1 = Cena1()
cena2 = Cena2()
cena1.connectDireita(cena1)
cena2.connectEsquerda(cena2)
