from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmadoka = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
linkportasparauniversos = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
gatocosmico = "http://i.imgur.com/RgaBeG7.png"
'''
def backdropcena():
  	cenaponto = Cena (img = linkbackdropcena)  
  	madoka = Elemento (img = linkpersonagem, tit="madoka")
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
    
backdropcena2()
'''
class Cena2():
	def __init__(self):
		self.cena = Cena(img = linkbackdropcena)
		#cena1 = Cena1()
  		madoka = Elemento (img = linkmadoka, tit="madoka", style = dict(right= 100, top=145, width= 115,bottom=20))
  		madoka.entra(self.cena)
  		txtmadoka = Texto(self.cena, "Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
  		madoka.vai = txtmadoka.vai
  		cenaponto = Cena (img = linkbackdropcena)
  		self.cena.meio = cenaponto
  		personagem_falecido = Elemento (img = gatocosmico, tit="Socorro!", style = dict(right= 100, top=200, width=75,bottom=50))
  		#personagem_falecido.entra(cenaponto)
  		gameover = Texto(cenaponto, "O Hubble Ultra Deep Field Ã© uma imagem de uma pequena regiÃ£o do espaÃ§o,na constelaÃ§Ã£o de Fornax, composta por dados do TelescÃ³pio Espacial Hubble no perÃ­odo de 3 de setembro de 2003 a 16 de janeiro de 2004. Ã a imagem mais profunda do universo tirada em luz visÃ­vel, ilustrando o universo tal como ele era hÃ¡ 13 bilhÃµes de anos atrÃ¡s.")
  		gameover.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena2().vai()