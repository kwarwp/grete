# grete.lisa.main.py
from _spy.vitollino.main import Cena,Elemento,Texto
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
BEACH = "http://casadeluxoemcamboinhas.com.br/wp-content/uploads/2015/01/28506.jpg"
FUNNYDOG = "https://image.redbull.com/rbcom/052/2017-09-01/6aef5132-28d4-418e-a85e-28e102b1cb22/0010/1/1500/1000/1/gente%2C-qual-a-necessidade-disso%3F.png"
DOLLYNHO = "https://lh3.ggpht.com/vshyoy6DTJtuLpXrqKesDJkJebNmpq7yTI-HUr7ICZ_jOe_xXBEWaGmYDrnbVDZxwA=w300"
CLASS23A = "https://i.imgur.com/DEWYjSJ.jpg"
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
borrifador_ = "https://i.imgur.com/PVBd6Zb.jpg"
vassoura_ = "https://i.imgur.com/mvUeaEl.jpg"
ampulheta_ = "https://i.imgur.com/cJA5pJD.jpg"
envelope_ = "https://i.imgur.com/GmMIxkq.jpg"
estojo_ = "https://i.imgur.com/Xz0C6PL.jpg"
TIRINHA_DO_CLAUDEMILSON = "https://i.imgur.com/yX187fL.jpg"
TRIG = None
def trigonometria():
    global TRIG
    if TRIG:
        return TRIG
        
    def _foi_geo():
        try:
            geografia().sul.vai()
        except:
            from naomi.main import geografia
            geografia().sul.vai()
        
    def _vai_geo():
        TRIG.sul.meio.vai = _foi_geo
        _vai = Cena(TIRINHA_DO_CLAUDEMILSON)
        def redir():
            _vai.vai = _foi_geo
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """The Lunch Kiddo!
Cleison pass throw the corridor but then he sees the 23 classroom lost dreams song.
the boy enters there and sees a different room: there’s a missing space! Then, Cleison
looks at the little door beside the board written “Become Robervald. Become Claudemilson.”,
He walks to the little door and he opens it: It’s the janitor’s room, weird… Cleison starts sneezing
all over the place, because it was too dirty , and at the same time, he was blowing the dust away, 
so he could see his locker, it was written “Lunch Kiddo”. A tear fell from his eye. He remembered 
Elianildes, an old canteen employee, and his friend too. After so much sentimentality, he heard a
noise inside the neighbour locker; he opened it and seen an afraid puppy, that Cleison called “Sadboy”,
but the dog was so excited! They were playing,when they heared a deafening sound of feet stepping on the 
floor. Sadboy ran away and Cleison was alone and without choice, when...
"""
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
        
    def vai_geo():
        _vai_geo()
    TRIG = _sala = Sala(CLASS23A,CLASS23B,CLASS23C,CLASS23D, "trig")
    from naomi.main import Elemento
    _sala.sul.meio = Cena(TIRINHA_DO_CLAUDEMILSON, vai = vai_geo)
    ampulheta = Elemento(ampulheta_, tit = "sprinkler", drag=True,
        x =500, y = 440, w = 60, h = 60, drop="hourglass",
        cena=_sala.leste, texto="please, help me, fix my name")
    estojo = Elemento(estojo_, tit = "broom", drag=True,
        x = 260, y = 410, w = 180, h = 100, drop="estojo",
        cena=_sala.leste, texto="please, help me, fix my name")
    borrifador = Elemento(borrifador_, tit = "envelope", drag=True,
        x =490, y = 390, w = 120, h = 130, drop="sprinkler",
        cena=_sala.sul, texto="please, help me, fix my name")
    envelope = Elemento(envelope_, tit = "pencilcase", drag=True,
        x = 100, y = 10, w = 80, h = 100, drop="envelope",
        cena=_sala.norte, texto="please, help me, fix my name")
    vassoura = Elemento(vassoura_, tit = "hourglass", drag=True,
        x = 44, y = 210, w = 280, h = 390, drop="broom",
        cena=_sala.oeste, texto="please, help me, fix my name")
        
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    trigonometria().norte.vai()
