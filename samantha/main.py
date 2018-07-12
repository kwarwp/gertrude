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
		self.__menu = Cena(img=IMG['patio']);
		start = Elemento(img = IMG['start'], style = dict(left=500, top=100, width= 100,bottom=20));
		lekes = Elemento(img=IMG['lekes'], style = dict(top = 50,right = 500, height = '250px' , width = 200))
		nana = Elemento(img=IMG['nana'], style = dict(top = 300,left = 510, height = '250px' , width = 180))
		leticia = Elemento(img=IMG['leticia'], style = dict(top = 300,left = 400, height = '250px' , width = 200))        
		Musica(sound = SOUNDS['background']);

		# Funcoes
		start.vai = Entrada().vai;
		lekes.vai=Texto(self.__menu ,"AndrÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ©- Cara, vocÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂª ouviu que o Jardim BotÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¢nico estÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¡ em manutenÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ§ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ£o?    Matheus- Sim, fiquei sabendo que coisas estranhas vem acontecendo lÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¡!").vai
		nana.vai=Texto(self.__menu,"Nana- Mas vocÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂª ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ© curiosa ein, e eu tambÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ©mÃÂÃÂÃÂÃÂ¢ÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¦ Vamos!").vai
		leticia.vai=Texto(self.__menu,"LetÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ­cia- Miga, vocÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂª viu que tem algo acontecendo no Jardim? Vamos lÃÂÃÂÃÂÃÂÃÂÃÂÃÂÃÂ¡ ver?").vai
        
		# Anexando elementos na cena
		start.entra(self.__menu);
		lekes.entra(self.__menu);
		leticia.entra(self.__menu);
		nana.entra(self.__menu);

	def vai(self): self.__menu.vai();

Menu().vai();