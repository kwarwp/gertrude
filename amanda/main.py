# gertrude.amanda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena2 = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkpersonagem = "https://dzy0ia.bn.files.1drv.com/y4mCpj--VWLV60iEJ-pMxcWj5qNmD4ADaUOa7--_3dCPywaXTvOJR7Swwev4gRzWeiKVPbGVm-hXYdZf4eLAnDy3jVcdztw1YRxwkrauYHHHssyFk3fBbjJQzZyal2cDRc6U0bQOj2TqfbMnibtNl5WjDt1T5WfApi0AWrm9HgZoSvELsvVsNE4BRRHcTpMxsUq0FA8RJjPi0YAHMD9Aa3Hyw/aaaaaaaaaaaa.png?psid=1"
linkcemiterio = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
personagem_morto = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_2944272726.png?disp=inline"
'''
def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2)  
  	personagem = Elemento (img = linkpersonagem)
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "e agora?")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	cenacemiterio = Cena (img = linkcemiterio)
  	cenaponto.direita = cenacemiterio
  	personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=125,bottom=20))
  	personagem_falecido.entra(cenacemiterio)
  	gameover = Texto(cenacemiterio, "Se ferrou!")
  	gameover.vai()
    
backdropcena2()
'''
class Cena2():
	def __init__(self):
		self.cena = Cena(img = linkbackdropcena2)
		#cena1 = Cena1()
  		personagem = Elemento (img = linkpersonagem)
  		personagem.entra(self.cena)
  		txtpersonagem = Texto(self.cena, "e agora?")
  		personagem.vai = txtpersonagem.vai
  		cenacemiterio = Cena (img = linkcemiterio)
  		self.cena.direita = cenacemiterio
  		personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=125,bottom=20))
  		personagem_falecido.entra(cenacemiterio)
  		gameover = Texto(cenacemiterio, "Se ferrou!")
  		gameover.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena2().vai()
