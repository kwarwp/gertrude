# gertrude.samantha.main.py
################################################TAKE0##########################################################

from _spy.vitollino.main import *
from kristen.main import Entrada
STYLE['width'] = 1000
STYLE['height'] = "600px"

IMG = {
	'start' : 'https://i0.wp.com/www.heversonbarbosa.com/wp-content/uploads/2017/05/home-seta.png',
	'patio' : "https://activufrj.nce.ufrj.br/file/GamesInteligentesII/20180710_111303.jpg?disp=inline",
	'lekes' : "http://3.bp.blogspot.com/-_JxmohXYIHI/Ud89A7TrTHI/AAAAAAAABQY/RGp-9STuc2c/s1600/pooh7.png",
	'nana' : "https://vignette.wikia.nocookie.net/monica4438/images/5/59/Magali.png/revision/latest?cb=20161221230552&path-prefix=es",
	'leticia' : "http://www.imagenspng.com.br/wp-content/uploads/2015/06/monica-02.png"
}

SOUNDS = {
	'background' : 'https://activufrj.nce.ufrj.br/file/GamesInteligentesII/Bia.mp3?disp=inline'
}

class Menu:

	def __init__(self):

		# Criando elementos
		self.__menu = Cena();
		start = Elemento(img = IMG['start'], style = dict(left=500, top=300, width= 100,bottom=20));
		lekes = Elemento(img=LEKES, style = dict(top = 50,right = 500, height = '250px' , width = 200))
		nana = Elemento(img=NANA, style = dict(top = 300,left = 510, height = '250px' , width = 180))
		leticia = Elemento(img=LETICIA, style = dict(top = 300,left = 400, height = '250px' , width = 200))        
		Musica(sound = SOUNDS['background']);

		# Funcoes
		start.vai = Entrada().vai;
		lekes.vai=Texto(self.__menu ,"AndrÃÂ©- Cara, vocÃÂª ouviu que o Jardim BotÃÂ¢nico estÃÂ¡ em manutenÃÂ§ÃÂ£o?    Matheus- Sim, fiquei sabendo que coisas estranhas vem acontecendo lÃÂ¡!").vai
		nana.vai=Texto(self.__menu,"Nana- Mas vocÃÂª ÃÂ© curiosa ein, e eu tambÃÂ©mÃ¢ÂÂ¦ Vamos!").vai
		leticia.vai=Texto(self.__menu,"LetÃÂ­cia- Miga, vocÃÂª viu que tem algo acontecendo no Jardim? Vamos lÃÂ¡ ver?").vai
        
		# Anexando elementos na cena
		start.entra(self.__menu);
		lekes.entra(self.__menu);
		leticia.entra(self.__menu);
		nana.entra(self.__menu);

	def vai(self): self.__menu.vai();

# Menu().vai();