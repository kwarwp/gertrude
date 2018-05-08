from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkpersonagem = "https://dzy0ia.bn.files.1drv.com/y4mCpj--VWLV60iEJ-pMxcWj5qNmD4ADaUOa7--_3dCPywaXTvOJR7Swwev4gRzWeiKVPbGVm-hXYdZf4eLAnDy3jVcdztw1YRxwkrauYHHHssyFk3fBbjJQzZyal2cDRc6U0bQOj2TqfbMnibtNl5WjDt1T5WfApi0AWrm9HgZoSvELsvVsNE4BRRHcTpMxsUq0FA8RJjPi0YAHMD9Aa3Hyw/aaaaaaaaaaaa.png?psid=1"
linkportasparauniversos = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
personagem_morto = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_2944272726.png?disp=inline"
'''
def backdropcena():
  	cenaponto = Cena (img = linkbackdropcena)  
  	personagem = Elemento (img = linkpersonagem, tit="marilyn monroe, style = dic(left= 0, top=0, width=0, height=0))
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "OlÃ¡, eu sou a ideia do bem e do mal.Esse Ã© um jogo de escolhas, sobre a breve histÃ³ria da humanidade.Para prosseguir clique no universo")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	cenacemiterio = Cena (img = linkcemiterio)
  	cenaponto.direita = cenaponto
  	personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=125,bottom=20))
  	personagem_falecido.entra(cenacemiterio)
  	gameover = Texto(cenacemiterio, "Se ferrou!")
  	gameover.vai()
    
backdropcena2()
'''
class Cena2():
	def __init__(self):
		self.cena = Cena(img = linkbackdropcena)
		#cena1 = Cena1()
  		personagem = Elemento (img = linkpersonagem, tit="marilyn monroe", style = dic(left= 0, top=0, width=0, height=0))
  		personagem.entra(self.cena)
  		txtpersonagem = Texto(self.cena, "OlÃ¡, eu sou a ideia do bem e do mal.Esse Ã© um jogo de escolhas, sobre a breve histÃ³ria da humanidade.Para prosseguir clique no universo")
  		personagem.vai = txtpersonagem.vai
  		cenaponto = Cena (img = linkbackdropcena)
  		self.cena.direita = cenaponto
  		personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=125,bottom=20))
  		personagem_falecido.entra(cenaponto)
  		gameover = Texto(cenaponto, "Se ferrou!")
  		gameover.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena2().vai()

