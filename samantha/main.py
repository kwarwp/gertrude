from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmadoka = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
linkportasparauniversos = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
gatocosmico = "http://i.imgur.com/RgaBeG7.png"
linkmarilyn = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"

def backdropcena():
  	cenaponto = Cena (img = linkbackdropcena)  
  	marilyn = Elemento (img = linkmarilyn, tit="marilyn")
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	cenacemiterio = Cena (img = linkcemiterio)
  	cenaponto.direita = cenaponto
  	personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=125,bottom=20))
  	personagem_falecido.entra(cenacemiterio)
  	gameover = Texto(cenacemiterio, "Se ferrou!")
  	gameover.vai()
'''    
backdropcena2()
'''
class Cena2():
	def __init__(self):
		self.cena = Cena(img = linkbackdropcena)
		#cena1 = Cena1()
  		marilyn = Elemento (img = linkmarilyn, tit="marilyn", style = dict(right= 100, top=145, width= 115,bottom=20))
  		marilyn.entra(self.cena)
  		txtmarilyn = Texto(self.cena, "Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
  		marilyn.vai = txtmarilyn.vai
  		cenaponto = Cena (img = linkbackdropcena)
  		self.cena.meio = cenaponto
  		personagem_falecido = Elemento (img = gatocosmico, tit="Socorro!", style = dict(right= 100, top=200, width=75,bottom=50))
  		#personagem_falecido.entra(cenaponto)
  		gameover = Texto(cenaponto, "O Hubble Ultra Deep Field ÃÂÃÂ© uma imagem de uma pequena regiÃÂÃÂ£o do espaÃÂÃÂ§o,na constelaÃÂÃÂ§ÃÂÃÂ£o de Fornax, composta por dados do TelescÃÂÃÂ³pio Espacial Hubble no perÃÂÃÂ­odo de 3 de setembro de 2003 a 16 de janeiro de 2004. ÃÂÃÂ a imagem mais profunda do universo tirada em luz visÃÂÃÂ­vel, ilustrando o universo tal como ele era hÃÂÃÂ¡ 13 bilhÃÂÃÂµes de anos atrÃÂÃÂ¡s.")
  		gameover.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena2().vai()