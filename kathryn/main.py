from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
LILLAPIZINHO="https://a-static.mlcdn.com.br/1500x1500/boneco-roblox-phantom-forces-ghost-brinquedos-chocolate/plazagames/1297/54d22d532df671e0503be50c285c0739.jpg"
MIDAS="https://images-eu.ssl-images-amazon.com/images/I/913LOf4vO3L.png"
class sambinha():
    lillapizinho= Elemento(img=LILLAPIZINHO)
    midas= Cena(img=MIDAS)
    lillapizinho.entra(midas)
    midas.vai()
sambinha()
