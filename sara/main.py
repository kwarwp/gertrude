# gertrude.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Texto 

linkbackdropcena2 = "http://s2.glbimg.com/yX02WqYevO4ETQxDkX8ReUFLfKk=/s.glbimg.com/jo/g1/f/original/2014/12/22/onibus-nathalia.jpg"
linkpersonagem = "https://vignette.wikia.nocookie.net/cartoonnetwork/images/4/48/Ad%C3%A3o_Le%C3%A3o_%281%29.png/revision/latest?cb=20150125151129&path-prefix=pt-br"
linkcemitario = "https://thumbs.dreamstime.com/z/cen%C3%A1rio-de-halloween-com-cemit%C3%A9rio-1-20146311.jpg

def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2)  
  	personagem = Elemento (img = linkpersonagem, tit="garotinho", style = dict(left= 150, top=100, width=60, height=200))
  	personagem.entra(cenaponto)
  	txtpersonagem = Texto(cenaponto, "e agora?")
  	personagem.vai = txtpersonagem.vai
  	cenaponto.vai()
  	planocemiterio = Plano (img = linkcemiterio)
  	planocemiterio.vai()
backdropcena2()

  
  
  
