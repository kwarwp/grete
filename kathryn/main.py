# grete.kathryn.main.py
from _spy.vitollino.main import Cena,Elemento,Texto, INVENTARIO, STYLE
STYLE.update(width=800, height="600px")
CLASS1 = "https://i.imgur.com/KsJNT1W.jpg"
CLASS2 = "https://i.imgur.com/ITXdLzJ.jpg"  # xJWIH1J.jpg"
CLASS3 = "https://i.imgur.com/P3iSUby.jpg"
CLASS4 = "https://i.imgur.com/m3UOcXX.jpg"
CORACAO = "https://i.imgur.com/6UKpUyW.jpg"
GLOBOS = "https://i.imgur.com/tzt1Ch4.jpg"
LEON   = "https://i.imgur.com/zUhR9wk.jpg"
# grete.amanda.main.py
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
interruptor = "https://i.imgur.com/5P3D5pp.jpg"
tomada = "https://i.imgur.com/FWRj0jJ.jpg"
monitor = "https://i.imgur.com/RgsKMmR.jpg"
parapeito = "https://i.imgur.com/r1wZeyw.jpg"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    TRIG = _sala = Sala(CLASS1,CLASS2,CLASS3,CLASS4, "trig")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    parap = Elemento(parapeito, tit = "microscope", drag=True,
        x = 610, y = 240, w = 80, h = 90, drop="glow ball",
        cena=_sala.norte, texto="please, help me, fix my name")
   
    interr = Elemento(interruptor, tit = "inter", drag=True,
        x = 500, y = 210, w = 80, h = 100, drop="earth globe",
        cena=_sala.sul, texto="please, help me, fix my name")
    
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()
'''
def aventurasnaescola():
    def gogeo(): 
        from naomi.main import geo_west
        geo_west()
    
    class1 = Cena (img = CLASS1)
    class2 = Cena (img = CLASS2)
    class3 = Cena (img = CLASS3)
    class4 = Cena (img = CLASS4)
    coracao = Cena (img = CORACAO)
    meio.vai = gogeo
    INVENTARIO.inicia()
    class1 = Cena(CLASS1)
    class2 = Cena(CLASS2, esquerda=class1)
    class3 = Cena(CLASS3, esquerda=class2)
    class4 = Cena(CLASS4, esquerda=class3, direita=class1)
    class1.esquerda, class1.direita = class4, class2
    class3.direita, class2.direita = class4, class3
    globos = Elemento(img = GLOBOS, tit = "globos", style = dict(left = 340, top = 55, widht = 55, height = 180))
    leon = Elemento(img = LEON, tit = "leon", style = dict(left = 350, top = 60, widht = 60, height = 200))
    leon.entra(class1)
    globos.entra(class1)
    txtleon = Texto(class1,"Eu quero viajar para cÃÂÂÂÃÂÂÂÂÂÂÂ¡!!")
    globos.entra(class2)
    leon.entra(class2)
    txtglobos = Texto(class2,"Ei,cuidado!!")
    globos.entra(class3)
    leon.entra(class3)
    txtleon = Texto(class3,"Desculpa!!")
    globos.entra(class4)
    leon.entra(class4)
    txtglobos = Texto(class4,"Vamos ser amiguinhos?!?!")
    globos.entra(coracao)
    leon.entra(coracao)
    txtleon = Texto(coracao,"Siiiiim!!!!!")
    txtglobos = Texto(coracao,"Siiiim!!!!!")
    class1.vai()
    
aventurasnaescola()

#ficha de prática ="https://i.imgur.com/n0hKsWn.jpg"
#objeto vermelho não identificado ="https://i.imgur.com/a9OjfFD.jpg"
#interruptor = "https://i.imgur.com/5P3D5pp.jpg"
#tomada = "https://i.imgur.com/FWRj0jJ.jpg"
#monitor = "https://i.imgur.com/RgsKMmR.jpg"
#parapeito = "https://i.imgur.com/r1wZeyw.jpg"
'''
     