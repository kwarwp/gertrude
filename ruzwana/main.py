from _spy.vitollino.main import Cena, Elemento, Texto 

linkbackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmarilyn = "https://activufrj.nce.ufrj.br/file/pedropeclat/WhatsApp_Image_2018-05-22_at_11.54.54.jpeg?disp=inline"
linkdeepspace = "https://www.google.com.br/search?q=deep+field&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjy2bbPu5nbAhXMhZAKHREpDnUQ_AUICigB&biw=1366&bih=662#imgrc=Ba3E_PaLJ3QRrM:"
linkmerlin = "https://activufrj.nce.ufrj.br/file/pedropeclat/00merlin-the-sword-in-the-stone-packing.png?disp=inline"
linkportasparauniversos = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
linkporta1 = "https://activufrj.nce.ufrj.br/file/pedropeclat/Dore.jpg?disp=inline"
#linkloba =
#linkporta2 =
linkmadoka = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
#linkporta3 =
#linkhipatia =
#linkporta4 =
linkbehelit ="https://vignette.wikia.nocookie.net/evil/images/3/3f/The_Behelit.jpg/revision/latest?cb=20151110185922"
linkend ="https://ia.media-imdb.com/images/M/MV5BNWM0OWRlNzctZDU5NS00ZDAzLWFkY2EtNDUxNjAxMjQ1ZWM4L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTY3Mzc2OTY@._V1_SX1777_CR0,0,1777,999_AL_.jpg"
linkgatocosmico = "http://i.imgur.com/RgaBeG7.png"



class Cena1():
	def __init__(self):
		self.cena = Cena(img = linkbackdropcena)
		#cena1 = Cena1()
  		marilyn = Elemento (img = linkmarilyn, tit="marilyn", style = dict(right= 100, top=145, width= 115,bottom=20))
  		marilyn.entra(self.cena)
  		txtmarilyn = Texto(self.cena, "Ola, eu sou a ideia do bem e do mal.Esse e um jogo de escolhas, sobre a breve historia da humanidade.Para prosseguir, clique no universo.")
  		marilyn.vai = txtmarilyn.vai
  		self.cenadeepspace = Cena (img = linkdeepspace)
  		self.cena.direita = cenadeepspace
  		cenadois = Texto(cenadeepspace, "O Hubble Ultra Deep Field uma imagem de uma pequena regiao do espaaço,na constelaçao de Fornax, composta por dados do Telescopio Espacial Hubble, 3 de setembro de 2003 a 16 de janeiro de 2004, a imagem mais profunda do universo tirada em luz visivel, ilustrando o universo tal como ele era a 13 bilhoeses de anos atras.")
  		cenadois.vai()
  		#self.cena.esquerda = cena1
	def vai(self, *_):
		self.cena.vai()

Cena1().vai()