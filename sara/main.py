# gertrude.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena2
linkbackdropcena2 = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/cena2_background.png?disp=inline"
linkpersonagem = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_2_9367638513.png?disp=inline"
linkcemiterio = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
personagem_morto = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_2944272726.png?disp=inline"
'''
def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2)  
  	personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 150, top=100, width=60, height=200))
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
	def __init__(self,escolha=False):
		self.cena = Cena(img = linkbackdropcena2)  
		cenacemiterio = Cena (img = linkcemiterio)
		#Cena 2
  		personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 150, top=100, width=60, height=200))
  		personagem.entra(self.cena)
  		txtpersonagem = Texto(self.cena, "Devo prosseguir meu caminho? (Clique na direita da cena para prosseguir)")
  		personagem.vai = txtpersonagem.vai
  		#Cena 3
  		personagem_falecido = Elemento (img = personagem_morto, tit="morreu", style = dict(right= 100, top=200, width=125,bottom=20))
  		personagem_falecido.entra(cenacemiterio)
  		gameover = Texto(cenacemiterio, "Se ferrou!")
  		gameover.vai()
		#Lógica
		if escolha: pass#self.cena.direita = #sucesso;
		else: self.cena.direita = cenacemiterio;
  		self.cena.esquerda = Cena1()
        
	def vai(self, *_):
		self.cena.vai()
    
