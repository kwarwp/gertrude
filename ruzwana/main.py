from _spy.vitollino.main import Cena, Elemento, Texto 

linkBackdropcena = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkmarilyn = "https://activufrj.nce.ufrj.br/file/pedropeclat/Mwindow.png?disp=inline"
linkdeepspace = "data:image/jpeg;base64,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"
linkmerlin = "https://activufrj.nce.ufrj.br/file/pedropeclat/00merlin-the-sword-in-the-stone-packing.png?disp=inline"
linkportasparauniversos = "https://universoracionalista.org/wp-content/uploads/2017/05/galaxias.jpg"
linkporta1 = "https://activufrj.nce.ufrj.br/file/pedropeclat/Dore.jpg?disp=inline"
linkbehelit ="https://activufrj.nce.ufrj.br/file/pedropeclat/The_Red_Behelit.png?disp=inline"
linkporta2 = "https://activufrj.nce.ufrj.br/file/pedropeclat/img.jpg?disp=inline"
linkmadoka = "https://images.puella-magi.net/c/ca/Madoka_main_page.png?20110119201909"
linkporta3 = " https://activufrj.nce.ufrj.br/file/pedropeclat/WhatsApp_Image_2018-05-28_at_17.14.57_1.jpeg?disp=inline"
linkhipatia ="https://activufrj.nce.ufrj.br/file/pedropeclat/image001.png?disp=inline"
linkporta4 ="https://activufrj.nce.ufrj.br/file/pedropeclat/39a95f77f7d60c9d383b2e63d5db83b8.jpg?disp=inline"
linkoppenheimer ="https://activufrj.nce.ufrj.br/file/pedropeclat/Oppenheimer.png?disp=inline"
linkend ="https://ia.media-imdb.com/images/M/MV5BNWM0OWRlNzctZDU5NS00ZDAzLWFkY2EtNDUxNjAxMjQ1ZWM4L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNTY3Mzc2OTY@._V1_SX1777_CR0,0,1777,999_AL_.jpg"
linkbojackesarahlynn=" https://activufrj.nce.ufrj.br/file/pedropeclat/21-bojack-11.png?disp=inline"
linkporta = "http://3.bp.blogspot.com/-i30OEIMf2Hk/URlDvN5bbcI/AAAAAAAAAhI/pO2GTPqTytc/s1600/door_3.png"
linkporta5 = "https://activufrj.nce.ufrj.br/file/pedropeclat/ae546a495e29ec5de4e18e63dbe68bab.jpg?disp=inline"
linkporta6 = "https://activufrj.nce.ufrj.br/file/pedropeclat/2d8213ffeae68105c808f0de97bc0a8c.jpg?disp=inline"
linkporta7 = "https://activufrj.nce.ufrj.br/file/pedropeclat/circle_of_angels_dantes_paradise_illustration.jpg?disp=inline"

def historia():
    cena1 = Cena(img = linkBackdropcena)
    marilyn = Elemento(img = linkmarilyn,tit="marilyn", style = dict(right= 100, top=90, width= 200,bottom=100,))
    marilyn.entra(cena1)
    txtmarilyn = Texto(cena1,"Ola, eu sou a ideia do bem e do mal. Esse eh um jogo de narrativo sobre a breve historia da humanidade.Para prosseguir, clique a direita no universo e para voltar clique a esquerda.")
    marilyn.vai=txtmarilyn.vai
    cena1.vai()
     
    cena2= Cena(img = linkdeepspace)
    merlin = Elemento (img = linkmerlin,tit="merlin", style = dict(left= 100, top=90, width= 115,bottom=20,))
    merlin.entra(cena2)
    txtmerlin = Texto(cena2,"O Hubble Ultra Deep Field eh uma imagem de uma pequena regiao do espaco, na constelacao de Fornax, composta por dados do Telescopio Espacial Hubble, 3 de setembro de 2003 ate o dia 16 de janeiro de 2004. Ela eh a imagem mais profunda do universo tirada em luz visivel, ilustrando o universo tal como ele era a 13 bilhoeses de anos atras.")
    merlin.vai = txtmerlin.vai
    
    cena1.direita = cena2
    cena2.esquerda = cena1
    
    cena3 = Cena(img = linkportasparauniversos)
    porta = Elemento(img = linkporta,tit = "porta",style = dict(left= 100, top=90, width= 115,bottom=20,))
    porta.entra(cena3)
    cena3.vai
    
    cena2.direita=cena3
    cena3.esquerda=cena2
    
    cena4 = Cena (img = linkporta1)
    behelit = Elemento (img = linkbehelit, tit = "behelit", style = dict(left= 100, top=90, width= 115,bottom=20,))
    behelit.entra(cena4)
    txtbehelit = Texto (cena4, "(Esse eh um quadro de Gustave Dore,The War Against Gibeon.)Ali, naquele palido cenario... É um pequeno palco onde uma especie vem se desenvolvendo durante anos, de caçadores e coletores a imperadores e reis")
    behelit.vai = txtbehelit.vai
    
    
    cena3.direita = cena4
    cena4.esquerda = cena3
    
    cena5 = Cena (img = linkporta5)
    
    cena4.direita=cena5
    cena5.esquerda=cena4
    
    cena6 = Cena (img = linkporta6)
    
    cena5.direita=cena6
    cena6.esquerda=cena5
    
    cena7 = Cena(img =linkporta7)
    
    cena6.direita=cena7
    cena7.esquerda=cena6
    
    
    cena8 = Cena (img = linkporta2)
    madoka = Elemento (img = linkmadoka, tit = "madoka",style = dict(right= 80, top=145, width= 115,bottom=20,))
    madoka.entra(cena8)
    txtmadoka = Texto (cena8, "Esse eh parthenon. Foi um templo dedicado a deusa grega Atena, construido no seculo V a.C. na Acropole de Atenas, na Grécia Antiga, por iniciativa de Pericles, governante da cidade. O Partenon é um símbolo duradouro da Grécia e da democracia, e é visto como um dos maiores monumentos culturais da história da humanidade. O nome Partenon deriva da estátua de Atena Partenos.")   
    madoka.vai = txtmadoka.vai
    
    cena7.direita=cena8
    cena8.esquerda=cena7
    
    cena9 = Cena (img = linkporta3)
    hipatia = Elemento (img = linkhipatia, tit ="hipatia",style = dict(left= 80, top=180, width= 115,bottom=20,))
    hipatia.entra(cena9)
    txthipatia = Texto (cena9, "Esse eh um quadro da Hilma af Klint, Group IX/SU")
    hipatia.vai = txthipatia.vai
    
    cena8.direita=cena9
    cena9.esquerda=cena8
    
    
    cena10 = Cena (img = linkporta4)
    oppenheimer = Elemento (linkoppenheimer, tit = "oppenheimer",style = dict(left= 100, top=90, width= 115,bottom=20,))
    oppenheimer.entra(cena10)
    txtoppenheimer = Texto(cena10,"Existe uma teoria que diz que, se um dia alguém descobrir exatamente para que serve o Universo e por que ele está aqui, ele desaparecerá instantaneamente e será substituído por algo ainda mais estranho e inexplicável. Existe uma segunda teoria que diz que isso já aconteceu")
    oppenheimer.vai = txtoppenheimer.vai
    
    
    cena9.direita=cena10
    cena10.esquerda=cena9
    
    cena11 = Cena (img =linkbojackesarahlynn)
    
    cena10.direita=cena11
    cena11.esquerda=cena10
    
    
    cena1.vai()
    
historia()
