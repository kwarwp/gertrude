# gertrude.samantha.main.pyfrom _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena
linkbackdropcena2 = "https://cdn.spacetelescope.org/archives/images/screen/heic0814a.jpg"
linkpersonagem = "https://vignette.wikia.nocookie.net/cartoonnetwork/images/4/48/Ad%C3%A3o_Le%C3%A3o_%281%29.png/revision/latest?cb=20150125151129&path-prefix=pt-br"
linkcemiterio = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
personagem_morto = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_2944272726.png?disp=inline"

def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2) 
  	personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 100, top=200, width=200, height=200))
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "e agora?")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	cenacemiterio = Cena (img = linkcemiterio)
  	cenaponto.direita = cenacemiterio
  	personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=300,bottom=20))
  	personagem_falecido.entra(cenacemiterio)
  	gameover = Texto(cenacemiterio, "Se ferrou!")
  	gameover.vai()
    
backdropcena2()

class Cena2():
	def __init__(self):   
 		cenaponto = Cena (img = linkbackdropcena2, tit="universo", style = dict(left=500, top=500, width=100, height=100))     
		self.cena = Cena(img = linkbackdropcena2)
		#cena1 = Cena1()
  		personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 50, top=200, width=300, height=200))
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