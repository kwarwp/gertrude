# gertrude.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Texto 

linkbackdropcena2 = "http://s2.glbimg.com/yX02WqYevO4ETQxDkX8ReUFLfKk=/s.glbimg.com/jo/g1/f/original/2014/12/22/onibus-nathalia.jpg"
linkpersonagem = "https://vignette.wikia.nocookie.net/cartoonnetwork/images/4/48/Ad%C3%A3o_Le%C3%A3o_%281%29.png/revision/latest?cb=20150125151129&path-prefix=pt-br"
linkcemiterio = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2)  
  	personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 150, top=100, width=60, height=200))
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "e agora?")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	planocemiterio = Plano (img = linkcemiterio)
  	Plano.vai()
backdropcena2()

  
  
  
