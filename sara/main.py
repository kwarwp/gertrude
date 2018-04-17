# gertrude.sara.main.py
from _spy.vitollino.main import Cena, Elemento, Texto 

linkbackdropcena2 = "http://s2.glbimg.com/yX02WqYevO4ETQxDkX8ReUFLfKk=/s.glbimg.com/jo/g1/f/original/2014/12/22/onibus-nathalia.jpg"
linkpersonagem = "https://vignette.wikia.nocookie.net/cartoonnetwork/images/4/48/Ad%C3%A3o_Le%C3%A3o_%281%29.png/revision/latest?cb=20150125151129&path-prefix=pt-br"

def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2)
  	cenaponto.vai()
  	personagem = garotinho (img = linkpersonagem)
  	personagem.entra(cenaponto)
backdropcena2()
  
  
  
