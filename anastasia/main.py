# grete.anastasia.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
TIRINHA_DO_CLAUDEMILSON = "https://i.imgur.com/yX187fL.jpg"
children = "https://i.imgur.com/SAjYpW5.jpg"
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
        gimnasium_.sul.meio.vai = _gone_gimnasiun
        _vai = Cena(TIRINHA_DO_CLAUDEMILSON)
        def redir():
            _vai.vai = _gone_gimnasiun
        historia = Cena(TIRINHA_DO_CLAUDEMILSON, _vai, _vai, _vai)
        texto = """Then when he stay house, he sit on the sofa,and turn on the TV and saw the following head line:
  - Manifestation on the street Dr. poop my pants.
 The manifestation is happening behind her house, and have peoples whif plates, turning down bus and screaming:
   - Became Robervald, became Claudemilson, became Robervald Claudemilson!!!!!!!!!!!!!!!
  He tired of all Claudemilson's and decide go sleep.
  Then he wake up at morning, and cout to her daddy and his mother of the crazy nightmare he has, and sit to turn on the TV and saw:
  - has a manifestation here the peoples are screaming: BECAME CLAUDEMILSON!!!!!!!!!!!!!!"""
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
        
    def go_gimnasiun():
        _go_gimnasiun()
        
    def __go_gimnasiun():
        from naomi.main import geografia
        geografia().sul.vai()
    gimnasium_ = _sala = Sala(gimnasium_n,gimnasium_l,gimnasium_s,gimnasium_o, "gimnasium")
    from naomi.main import Elemento
    _sala.sul.meio.vai = go_gimnasiun
    children_ = Elemento(children, tit = "reflector", drag=True,
        x = 200, y = 188, w = 150, h = 200, drop="children",
        cena=_sala.sul, texto="please, help me, fix my name")
    bars_ = Elemento(bars, tit = "grandstand", drag=True,
        x = 160, y = 210, w = 80, h = 100, drop="bars",
        cena=_sala.norte, texto="please, help me, fix my name")
    grandstand_ = Elemento(grandstand, tit = "bars",
        x = 360, y = 70, w = 80, h = 70, drop="grandstand",
        cena=_sala.oeste, texto="please, help me, fix my name")
    reflector_ = Elemento(reflector, tit = "ball", drag=True,
        x = 300, y = 275, w = 100, h = 140, drop="reflector",
        cena=_sala.norte, texto="please, help me, fix my name")
    light_post_ = Elemento(light_post, tit = "children", drag=True,
        x = 50, y = 40, w = 100, h = 100, drop="light_post",
        cena=_sala.sul, texto="please, help me, fix my name")
    ball_ = Elemento(ball, tit = "ligthpost",
        x = 400, y = 300, w = 100, h = 120,drop="ball",
        cena=_sala.norte, texto="please, help me, fix my name")
    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    gimnasium().norte.vai()
