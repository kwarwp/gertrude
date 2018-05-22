#jaspe/main.py
from _spy.vitollino.main import Cena, Elemento, Texto
import time

l = 300

img_cena1 = "https://media.giphy.com/media/l0HlRVFefdU4nygus/giphy.gif"
img_cena2 = "https://media.giphy.com/media/bHoFqabfGJLpu/giphy.gif"
img_cena3 = "https://media.giphy.com/media/AxlEMZ8HQxPbO/giphy.gif"
img_cena4 = "https://media.giphy.com/media/3lEhfN49gSyw8/giphy.gif"
img_cena5 = "https://media.giphy.com/media/718jMaARpUgiQ/giphy.gif"
img_cena6 = "https://media.giphy.com/media/26gsspfbt1HfVQ9va/giphy.gif"

elementoViraPagina = "http://www.clker.com/cliparts/J/w/2/4/N/p/page-curl-md.png"

elemento_cena1 = "https://pbs.twimg.com/profile_images/910649920989859841/6TTyYmF9_400x400.jpg"
#elemento_cena2 = "http://www.onlygfx.com/wp-content/uploads/2017/04/grunge-brush-stroke-banner-2-4-1024x264.png"
#elemento_cena3 = "https://i1.wp.com/res.cloudinary.com/aleteia/image/fetch/c_fill,g_auto/https://aleteiaen.files.wordpress.com/2017/06/triquetra-circle-interlaced.png?resize=0%2C0&quality=100&strip=all&ssl=1"
#elemento_cena4 = "http://dareid.github.io/chakram/assets/circle_brush_white.png"


linkRippleWater = "https://thumbs.gfycat.com/MarvelousAdolescentIndianringneckparakeet-size_restricted.gif"
linkArvoreVida = "http://www.pennsvalleypharmacy.com/wp-content/uploads/2016/07/Tree-of-Life-png.png"
linkFlow = "https://media.giphy.com/media/IspWIAkPbgRKU/giphy.gif"
linkSabio = "http://www.zamolski.com/agot/resources/images/portraits/wiseman.png"
linkFestival = "http://www.vietnamtourism.com/imguploads/news/2016/T10/LHAnhsanhAnDo.jpg"
linkEngrenagem = "https://3.bp.blogspot.com/-3JjRwCMwZek/WWjhEkvMguI/AAAAAAAAAQ8/6mlLfOdZKcsWB9wA4VZp0QURmybxidHjgCLcBGAs/s1600/FuzzyTube.gif"

def Mito():
    
    viuCenas = [ False, False, False, False, False, False]
    cena1 = Cena(img = img_cena1)
    simbolo1 = Elemento(img = elemento_cena1, style = dict(top = 150, bottom = 10, left = 100, width = 150))
    texto1 = Texto(cena1, "Quem sabe faz ao vivo, Meuuu")
    simbolo1.vai = texto1.vai
    simbolo1.entra(cena1)
    cena1vaiOriginal = cena1.vai
    
    def novaCena1Vai():
        cena1vaiOriginal()
        if viuCenas[0] == False:
            texto1.vai()
            viuCenas[0] = True
            
    cena1.vai = novaCena1Vai
    
    
    cena2 = Cena(img = img_cena2)
#    simbolo2 = Elemento(img = elemento_cena2, style = dict(top = 130, bottom = 10, left = 98, width = 90))
    texto2 = Texto(cena2, "Martysex")
#    simbolo2.vai = texto2.vai
#    simbolo2.entra(cena2)
    cena2vaiOriginal = cena2.vai
    
    def novaCena2Vai():
        cena2vaiOriginal()
        if viuCenas[1] == False:
            texto2.vai()
            viuCenas[1] = True
            
    cena2.vai = novaCena2Vai
    cena1.direita = cena2
    cena2.esquerda = cena1
    
    cena3 = Cena(img = img_cena3)
#    simbolo3 = Elemento(elemento_cena3, style = dict(top = 100, bottom = 10, left = 100, width = 100))
    texto3 = Texto(cena3, "Shark-ira")
#    simbolo3.vai = texto3.vai
#    simbolo3.entra(cena3)
    cena3vai = cena3.vai
    
    cena3vaiOriginal = cena3.vai
    
    def novaCena3Vai():
        cena3vaiOriginal()
        if viuCenas[2] == False:
            texto3.vai()
            viuCenas[2] = True
            
    cena3.vai = novaCena3Vai
    
    cena2.direita = cena3
    cena3.esquerda = cena2
    
    
    cena4 = Cena(img = img_cena4)
#    simbolo4 = Elemento(elemento_cena4, style = dict(top = 100, bottom = 10, left = 100, width = 100))
    texto4 = Texto(cena4, "Osama")
#    simbolo4.vai = texto4.vai
#    simbolo4.entra(cena4)

    cena4vai = cena4.vai
    
    cena4vaiOriginal = cena4.vai
    
    def novaCena4Vai():
        cena4vaiOriginal()
        if viuCenas[3] == False:
            texto4.vai()
            viuCenas[3] = True
            
    cena4.vai = novaCena4Vai

    cena3.direita = cena4
    cena4.esquerda = cena3
    
    cena5 = Cena(img = img_cena5)
#    simbolo5 = Elemento(elemento_cena5, style = dict(top = 100, bottom = 10, left = 100, width = 100))
    texto5 = Texto(cena5, "Romano")
#    simbolo5.vai = texto5.vai
#    simbolo5.entra(cena5)

    cena5vai = cena5.vai
    
    cena5vaiOriginal = cena5.vai
    
    def novaCena5Vai():
        cena5vaiOriginal()
        if viuCenas[4] == False:
            texto5.vai()
            viuCenas[4] = True
            
    cena5.vai = novaCena5Vai

    cena4.direita = cena5
    cena5.esquerda = cena4

    cena6 = Cena(img = img_cena6)
#    simbolo6 = Elemento(elemento_cena6, style = dict(top = 100, bottom = 10, left = 100, width = 100))
    texto6 = Texto(cena6, "Acertouuu")
#    simbolo6.vai = texto6.vai
#    simbolo6.entra(cena6)

    cena6vai = cena6.vai
    
    cena6vaiOriginal = cena6.vai

    def novaCena6Vai():
        cena6vaiOriginal()
        if viuCenas[5] == False:
            texto6.vai()
            viuCenas[5] = True
            
    cena6.vai = novaCena6Vai

    cena5.direita = cena6
    cena6.esquerda = cena5




    
    cena1.vai()
    
Mito()