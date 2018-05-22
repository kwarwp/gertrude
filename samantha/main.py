from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmadoka = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
linkportasparauniversos = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
gatocosmico = "http://i.imgur.com/RgaBeG7.png"
linkmarilyn = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
linkdeepspace = "https://www.google.com.br/search?q=deep+field&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjy2bbPu5nbAhXMhZAKHREpDnUQ_AUICigB&biw=1366&bih=662#imgrc=Ba3E_PaLJ3QRrM:"

def backdropcena():
  	cenaponto = Cena (img = linkbackdropcena)  
  	marilyn = Elemento (img = linkmarilyn, tit="marilyn")
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	cenadeepspace = Cena (img = linkdeepspace)
  	cenamarilyn.direita = cenadeepspace
  	gameover = Texto(cenacemiterio, "O Hubble Ultra Deep Field uma imagem de uma pequena regiao do espaço,na constelaçao de Fornax, composta por dados do Telescopio Espacial Hubble, 3 de setembro de 2003 a 16 de janeiro de 2004, a imagem mais profunda do universo tirada em luz visivel, ilustrando o universo tal como ele era a 13 bilhoeses de anos atras.")
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
  		cenadeepspace = Cena (img = linkdeepspace)
  		self.cena.meio = cenadeepspace
  		gameover = Texto(cenadeepspace, "O Hubble Ultra Deep Field uma imagem de uma pequena regiao do espaço,na constelaçao de Fornax, composta por dados do Telescopio Espacial Hubble, 3 de setembro de 2003 a 16 de janeiro de 2004, a imagem mais profunda do universo tirada em luz visivel, ilustrando o universo tal como ele era a 13 bilhoeses de anos atras.")
  		gameover.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena2().vai()