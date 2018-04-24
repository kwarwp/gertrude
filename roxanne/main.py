# gertrude.roxanne.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE

w = 300
STYLE['width'] = w
STYLE['height'] = w
linkCena = ""
linkObjeto = "https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F891279159%2Ficons%2Fon_color_large.png%3Fversion%3D0?ixlib=rails-2.1.3&w=240&h=240&auto=compress&s=8e9316a345ccb3bf6569068e4e025d23"

def mockCena():
  mCena = Cena(img = linkCena)
  mObj = Elemento(img = linkObjeto)
  mObj.entra(mCena, style = dict(width = 30, bottom = 200))
  mCena.vai()
mockCena()
  
  
  
  
  
  