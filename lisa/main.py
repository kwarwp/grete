# grete.lisa.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
BEACH = "http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg"
FUNNYDOG = "https://image.redbull.com/rbcom/052/2017-09-01/6aef5132-28d4-418e-a85e-28e102b1cb22/0010/1/1500/1000/1/gente%2C-qual-a-necessidade-disso%3F.png"
DOLLYNHO = "https://lh3.ggpht.com/vshyoy6DTJtuLpXrqKesDJkJebNmpq7yTI-HUr7ICZ_jOe_xXBEWaGmYDrnbVDZxwA=w300"
CLASS23A = ""
CLASS23B = "https://i.imgur.com/N5A2DAb.jpg"
CLASS23C = "https://i.imgur.com/zP65MT5.jpg"
CLASS23D = "https://i.imgur.com/NLkvCsx.jpg"
'''
 INVENTARIO.inicia()
    n_trig = Cena(CLASS23A)
    e_trig = Cena(CLASS23B, esquerda=n_trig)
    s_trig = Cena(CLASS23C, esquerda=e_trig, meio=Cena(vai=vai_geo))
    o_trig = Cena(CLASS23D, esquerda=s_trig, direita=n_trig)
    n_trig.esquerda, n_trig.direita = o_trig, e_trig
    s_trig.direita, e_trig.direita = o_trig, s_trig

def dogatthebeach():
    beach = Cena ("http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg")
    funnydog = Elemento("http://www.instatube.com.br/wp-content/uploads/2015/08/pugs-mais-engracados-do-mundo-vi-480x293.jpg", tit = "FUNNYDOG",  style = dict(left = 150, top = 60, widht = 60, height = 200))
    txtfunnydog = Texto(beach,"Do you need dolly?")
    funnydog.entra(beach)
    funnydog.vai = txtfunnydog.vai
    beach.vai()
    
    
dogatthebeach()
'''
borrifador = "https://i.imgur.com/PVBd6Zb.jpg"
vassoura = "https://i.imgur.com/mvUeaEl.jpg"
ampulheta = "https://i.imgur.com/cJA5pJD.jpg"
envelope = "https://i.imgur.com/GmMIxkq.jpg"
estojo = "https://i.imgur.com/Xz0C6PL.jpg"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def vai_geo():
        from naomi.main import geografia
        geografia().sul.vai()
    TRIG = _sala = Sala(CLASS23A,CLASS23B,CLASS23C,CLASS23D, "trig")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_geo
    sweeper = Elemento(vassoura, tit = "microscope", drag=True,
        x =4, y = 240, w = 280, h = 390, drop="glow ball",
        cena=_sala.oeste, texto="please, help me, fix my name")
    pencil = Elemento(estojo, tit = "volcano", drag=True,
        x = 260, y = 210, w = 180, h = 100, drop="earth globe",
        cena=_sala.leste, texto="please, help me, fix my name")
    '''
    volc = Elemento(volcano, tit = "glow ball", drop="volcano",
        x = 30, y = 500, w = 100, h = 120,
        cena=_sala.leste, texto="please, help me, fix my name")
        '''
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()
