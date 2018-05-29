# gertrude.kellee.main.py
from _spy.vitollino.main import Cena, Texto, Elemento

linkCaverna = "http://tolongedecasa.com/wp-content/uploads/2017/07/Caverna-de-Postonja-21.jpg"
linkGolem = "https://vignette.wikia.nocookie.net/soulcalibur/images/d/dc/Golem.jpg"

def Defumado():
    caverna = Cena(img = linkCaverna)
    Golem = Elemento(img = linkGolem, tit="Golem", style=dict(left= 120, top= 150, width= 100,height= 250))
    Golem.entra(caverna)
    txtGolem=Texto(caverna, "Sim meu mestre!")
    Golem.vai = txtGolem.vai
    caverna.vai()
    
    linkFloresta = "http://www.cashcar.com.br/wp-content/uploads/2016/11/Floresta-da-Tijuca.jpg"

    floresta = Cena(img=linkFloresta)
    Golem2 = Elemento(img = linkGolem, style =dict(top = 150, left = 120, height = 250, width = 100))
    Golem2.entra(floresta)
    txtGolem2 = Texto(floresta, "Irei atrás da caça para me alimentar, talvez na cidade!")
    Golem2.vai = txtGolem2.vai
    
    caverna.direita = floresta
    floresta.esquerda = caverna 
    
    linkBerlim = "https://i1.wp.com/mochilaobarato.com.br/wp-content/uploads/2016/09/Berlim-2.jpg"
    
    berlim = Cena(img=linkBerlim)
    Golem3 = Elemento(img = linkGolem, style =dict(top = 150, left = 120, height = 250, width = 100))
    Golem3.entra(berlim)
    txtGolem3 = Texto(berlim, "A cidade irá ficar diante dos meus pés!")
    Golem3.vai = txtGolem3.vai
    
    floresta.direita = berlim
    berlim.esquerda = floresta
    
    linkMago = "https://i.pinimg.com/236x/b2/78/23/b2782362865728f0b36253ec13f7e2da.jpg"
    linkMistica = "https://f4.bcbits.com/img/a3080013838_16.jpg"
    
    Mistica = Cena(img = linkMistica)
    Mago = Elemento(img = linkMago, tit="Mago", style=dict(left= 120, top= 150, width= 100, height= 250))
    Mago.entra(Mistica)
    txtMago=Texto(Mistica, "Onde andas minha criação?")
    Mago.vai = txtMago.vai
    
    berlim.direita = Mistica
    Mistica.esquerda = berlim
    
    linkAmiguinho = "https://pbs.twimg.com/profile_images/3382643320/5e7323e465d26ebdddf2cab4c5b26c31.jpeg"
    
    berlim2 = Cena(img = linkBerlim)
    Amiguinho = Elemento(img = linkAmiguinho, style =dict(top = 150, left = 120, height = 250, width = 100))
    Amiguinho.entra(berlim2)
    txtAmiguinho=Texto(berlim2, "Quem há de entrar em minha morada? Yo soy Dollynho!")
    Amiguinho.vai = txtAmiguinho.vai
    
    Mistica.direita = berlim2
    berlim2. esquerda = Mistica
    
    berlim3 = Cena(img=linkBerlim)
    Golem4 = Elemento(img=linkGolem, style = dict( top = 150, left = 120, height = 250, width = 100))
    txtGolem4 = Texto(berlim3, "Essa cidade é pequena demais pra nois dois, meu brodi!")
    Golem4.entra(berlim3)
    Golem4.vai = txtGolem4.vai
    
    berlim2.direita = berlim3
    berlim3.esquerda = berlim2
    
    berlim4 = Cena(img=linkBerlim)
    Golem5 = Elemento(img = linkGolem, style =dict(top = 150, left = 160, height = 250, width = 100))
    Amiguinho2 = Elemento(img = linkAmiguinho, style =dict(top = 150, left = 20, width = 100, height = 250))
    Golem5.entra(berlim4)
    Amiguinho2.entra(berlim4)
    txtAmiguinho2=Texto(berlim4, "Veremos ver quem irá ficar com o território!")
    Amiguinho2.vai = txtAmiguinho2.vai
    
    berlim3.direita = berlim4
    berlim4.esquerda = berlim3
    
    caverna.vai()
    
Defumado()
    