# grete.kathryn.main.py
#TIRINHA E TEXTO
#REVISADO PRONTO
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
TIRINHA_DO_CLAUDEMILSON ="https://i.imgur.com/2krCeWj.png"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def _gone_geography():
        try:
            geography().oeste.vai()
        except:
            from naomi.main import geografia as geography
            geography().oeste.vai()
    def _go_trigonometria():
        TRIG.norte.meio = Cena(vai=_gone_geography)
        _vai = Cena()
        def redir():
            _vai.vai = _gone_geography
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """ Cleison decides to go to the computer to see videos of kittens. As he sat on the chair, 
        he slapped his arm on the sill.Ouch, it hurts. - The sill say. - I am Sorry.  Says Cleison - It is so
        dark in here, I will turn on the lights. When he turns it on:- Ouch!!Cried the switch. Sorry again. 
        Why do you feel so much pain? It is because Claudemilson cast a spell on us and now we feel pain 
        all the time.But why does she do that??? It is because when we feel pain we are pro-Claudemilson.
 """ 
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()        
        
    def go_trigonometria():
        _go_trigonometria()   
        
    def go_geography():
        try:
            geography().norte.vai()
        except:
            from naomi.main import geografia as geography
            geography().oeste.vai()
    TRIG = _sala = Sala(CLASS1,CLASS2,CLASS3,CLASS4, "trig")
    from naomi.main import Elemento
    _sala.leste.meio = Cena(vai=go_trigonometria)
    #_sala.oeste.meio.vai = _go_geography
    parap = Elemento(parapeito, tit = "socket", drag=True,
        x = 610, y = 300, w = 80, h = 90, drop="sill",
        cena=_sala.norte, texto="Please help me, fix my name.")

    interr = Elemento(interruptor, tit = "sill", drag=True,
        x = 360, y = 160, w = 40, h = 70, drop="light switch",
        cena=_sala.leste, texto="Please help me, fix my name.")
    
    toma = Elemento(tomada, tit = "screen", drag=True,
        x = 100, y = 300, w = 60, h = 70, drop="socket",
        cena=_sala.sul, texto="Please help me, fix my name.")
        
    mono = Elemento(monitor, tit = "light switch", drag=True,
        x = 105, y = 335, w = 90, h = 80, drop="screen",
        cena=_sala.oeste, texto="Please help me, fix my name.")
    
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
    txtleon = Texto(class1,"Eu quero viajar para cÃÂÂÂÂÂÂÂÂÂÂÃÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂ¡!!")
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
     