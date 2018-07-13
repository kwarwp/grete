# grete.morgan.main.py
Principals_room_n = "https://i.imgur.com/U9ixbT0.jpg"
Principals_room_o = "https://i.imgur.com/gxOcDsS.jpg"
Principals_room_l = "https://i.imgur.com/SV1Ko1N.jpg"
Principals_room_s = "https://i.imgur.com/V85pfUS.jpg"
principalsroom_ = None #"https://i.imgur.com/UsGRBIp.jpg"
# objects
clips = "https://i.imgur.com/Z25C40V.jpg"
door_lock = "https://i.imgur.com/q1tJiqJ.jpg"
keyboard = "https://i.imgur.com/EM4mZq2.jpg"
power_plug ="https://i.imgur.com/4eX2x0y.jpg"
pipe = "https://i.imgur.com/IWX6ah1.jpg"
caixa_mae = "https://i.imgur.com/THLu9uv.jpg"
from _spy.vitollino.main import STYLE, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
PRR = None
def principalsroom():
    global principalsroom_
    if principalsroom_:
        return principalsroom_
        
    def _gone_principalsroom():
        try:
            gymnasium().sul.vai()
        except:
            from libby.main import gymansium
            gymnasium().sul.vai()
        def _go_principalsroom():
            principalsroom_.sul.meio.vai = _gone_principalsroom
            _vai = Cena(PRINCIPALS_ROOM)
        def redir():
            _vai.vai = _principalsroom
        historia = Cena(PRINCIPALS_ROOM, _vai, _vai, _vai)
        texto = """                        Cleison goes to the principalÃÂ´s room
Cleison hears someone calling him. He did not know who it was. He looked and saw a woman wearing a t-shirt with the words : Become Claudemilson. 
She said:
-Go to the PrincipalÃÂ´s room!!!!
He remembered that  in his time he had a principal named George that was cool.
He did not understand anything, only followed the woman. In the principalÃÂ´s room, she said
-You will have to listen to a rap and a funk of the dictatorship of Claudemilson and eat raw noodles!!!
Out of nowhere started a beat: Become ClaudemilsonÃ¢ÂÂ« Ã¢ÂÂª
Wile Claudemilson was not seeing, Claison escaped.
When he ran away, he got into his car and went around desperately, but a traffic policeman stopped him . In this meanwhile, Claudemilson had time to reach him.Claudemilson began to shout with Cleison and in the meantime a fiscal that passed near there decided to enter the school .He saw that Claudemilson tortured the children, and she was arrested.
""" 
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
        
    PRR = _sala = Sala(Principals_room_n,Principals_room_o,Principals_room_l,Principals_room_s, "principal")
    from naomi.main import Elemento
    _sala.sul.meio.vai = vai_principalsroom
    caixa = Elemento(caixa_mae, tit = "pipe", drag=True,
        x = 480, y = 140, w = 180, h = 290, drop="glow ball",
       cena=_sala.norte, texto="please, help me, fix my name")
    clip  = Elemento(clips, tit = "power plug", drag=True,
        x = 260, y = 410, w = 80, h = 100, drop="clips",
        cena=_sala.leste, texto="please, help me, fix my name")

    pipes = Elemento(pipe, tit = "router rack", drop="cano",
        x = 500, y = 5, w = 100, h = 120,
        cena=_sala.norte, texto="please, help me, fix my name")
    power = Elemento(power_plug, tit = "locker", drag=True,
        x = 510, y = 360, w = 100, h = 90, drop="glow ball",
       cena=_sala.leste, texto="please, help me, fix my name")
    doorl = Elemento(door_lock, tit = "keyboard", drag=True,
        x = 440, y = 380, w = 80, h = 100, 
        cena=_sala.sul, texto="please, help me, fix my name")
    keyboard_ = Elemento(keyboard, tit = "clip", drop="keyboard",
        x = 300, y = 300, w = 100, h = 70,
        cena=_sala.leste, texto="please, help me, fix my name")

    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    principalsroom().norte.vai()