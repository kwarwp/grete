# grete.anastasia.main.py
# REVISADO PRONTO
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
TIRINHA_DO_CLAUDEMILSON = "https://i.imgur.com/vIYgSQV.jpg"
child = "https://i.imgur.com/SAjYpW5.jpg"
bars = "https://i.imgur.com/4g9dJdv.jpg"
grandstand = "https://i.imgur.com/6PYwS0s.jpg"
reflector = "https://i.imgur.com/U41sbtV.jpg"
light_post = "https://i.imgur.com/Jk68bvK.jpg"
ball = "https://i.imgur.com/bMUHNdH.jpg"
gimnasium_l = "https://i.imgur.com/RVIqCjp.jpg"
gimnasium_o = "https://i.imgur.com/kdnYpkh.jpg"
gimnasium_n = "https://i.imgur.com/befIyyM.jpg"
gimnasium_s = "https://i.imgur.com/5SnGZmp.jpg"
gimnasium_ = None
def gimnasium():
    global gimnasium_
    if gimnasium_:
        return gimnasium_
        
    def _gone_gimnasiun():
        try:
            secretary().sul.vai()
        except:
            from libby.main import secretary
            secretary().sul.vai()
        
    def _go_gimnasiun():
        gimnasium_.norte.meio = Cena(vai=_gone_gimnasiun)
        _vai = Cena()
        def redir():
            _vai.vai = _gone_gimnasiun
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """ One day, there was a manifestation against Claudemilson, and she didn't like it. She made the people of the manifestation hear Funk Carioca during 10 hours. """ 
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
        
    def go_gimnasiun():
        _go_gimnasiun()
        
    def go_school_house():
        try:
            school_house_().norte.vai()
        except:
            from courtney.main import school_house_
            school_house_().norte.vai()
        
    def go_geography():
        try:
            geografia().norte.vai()
        except:
            from naomi.main import geografia
            geografia().norte.vai()

        
    def __go_gimnasiun():
        from naomi.main import geografia
        geografia().sul.vai()
    gimnasium_ = _sala = Sala(gimnasium_n,gimnasium_l,gimnasium_s,gimnasium_o, "gimnasium")
    from naomi.main import Elemento
    _sala.norte.meio = Cena(vai=go_gimnasiun)
    _sala.oeste.meio = Cena(vai=go_school_house)
    _sala.sul.meio = Cena(vai=go_geography)
    child_ = Elemento(child, tit = "reflector", drag=True,
        x = 210, y = 160, w = 334, h = 213, drop="child",
        cena=_sala.sul, texto="please, help me, fix my name")
    bars_ = Elemento(bars, tit = "grandstand", drag=True,
        x = 375, y = 3, w = 130, h = 70, drop="bars",
        cena=_sala.norte, texto="please, help me, fix my name")
    grandstand_ = Elemento(grandstand, tit = "bars",
        x = 330, y = 188, w = 187, h = 180, drop="grandstand",
        cena=_sala.oeste, texto="please, help me, fix my name")
    reflector_ = Elemento(reflector, tit = "ball", drag=True,
        x = 700, y = 13, w = 100, h = 140, drop="reflector",
        cena=_sala.oeste, texto="please, help me, fix my name")
    light_post_ = Elemento(light_post, tit = "child", drag=True,
        x = 300, y = 2, w = 400, h = 380, drop="lightpost",
        cena=_sala.leste, texto="please, help me, fix my name")
    ball_ = Elemento(ball, tit = "lightpost",
        x = 358, y = 210, w = 40, h = 40,drop="ball",
        cena=_sala.norte, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    gimnasium().norte.vai()
