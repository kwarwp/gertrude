from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmadoka = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
linkportasparauniversos = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
personagem_morto = "http://i.imgur.com/RgaBeG7.png"

class Cena2():
	def __init__(self):
		self.cena = Cena(img = linkbackdropcena)
		#cena1 = Cena1()
  		madoka = Elemento (img = linkmadoka, tit="madoka", style = dict(right= 100, top=145, width= 115,bottom=20))
  		madoka.entra(self.cena)
  		txtpersonagem = Texto(self.cena, "Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
  		madoka.vai = txtpersonagem.vai
  		cenaponto = Cena (img = linkbackdropcena)
  		self.cena.meio = cenaponto
  		personagem_falecido = Elemento (img = personagem_morto, tit="Socorro!", style = dict(right= 100, top=200, width=75,bottom=50))
  		personagem_falecido.entra(cenaponto)
  		gameover = Texto(cenaponto, "Se ferrou!")
  		gameover.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena2().vai()

