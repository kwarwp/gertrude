# gertrude.samantha.main.pyfrom _spy.vitollino.main import Cena, Elemento, Texto 
#from julia.main import Cena1
#Cena
linkbackdropcena2 = "https://cdn.spacetelescope.org/archives/images/screen/heic0814a.jpg"
linkpersonagem = "https://vignette.wikia.nocookie.net/cartoonnetwork/images/4/48/Ad%C3%A3o_Le%C3%A3o_%281%29.png/revision/latest?cb=20150125151129&path-prefix=pt-br"
linkcemiterio = "https://static.brusheezy.com/system/resources/premium_previews/000/041/258/non_2x/Eerie-Halloween-Wallpaper-PSD.jpg"
personagem_morto = "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/imageedit_1_2944272726.png?disp=inline"

def backdropcena2():
  	cenaponto = Cena (img = linkbackdropcena2,tit="universo", style = dict(left=500, top=500, width=100, height=100)) 