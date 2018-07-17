# grete.morgan.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE,Dragger, Droppable, INVENTARIO, Sala
STYLE["width"] = 800
STYLE["height"] = "600px"
TIRINHA_PRINCIPALS_ROOM = "https://i.imgur.com/UsGRBIp.jpg"
Principals_room_n = "https://i.imgur.com/U9ixbT0.jpg"
Principals_room_o = "https://i.imgur.com/gxOcDsS.jpg"
Principals_room_l = "https://i.imgur.com/SV1Ko1N.jpg"
Principals_room_s = "https://i.imgur.com/V85pfUS.jpg"
principalsroom_ = None #"https://i.imgur.com/UsGRBIp.jpg"
# objects
clips_ = "https://i.imgur.com/Z25C40V.jpg"
door_lock = "https://i.imgur.com/q1tJiqJ.jpg"
keyboard = "https://i.imgur.com/EM4mZq2.jpg"
power_plug ="https://i.imgur.com/4eX2x0y.jpg"
pipe_ = "https://i.imgur.com/IWX6ah1.jpg"
caixa_mae = "https://i.imgur.com/THLu9uv.jpg"

PRR = None
def principalsroom():
    global principalsroom_
    if principalsroom_:
        return principalsroom_
        
    def _gone_principalsroom():
        try:
            principalsroom().sul.vai()
        except:
            from libby.main import gymnasium
            gymnasium().sul.vai()
    def _go_principalsroom():
        principalsroom_.sul.meio.vai = _gone_principalsroom
        _vai = Cena(TIRINHA_PRINCIPALS_ROOM)
        def redir():
            _vai.vai = _gone_principalsroom
        historia = Cena(TIRINHA_PRINCIPALS_ROOM, _vai, _vai, _vai)
        texto = """Cleison goes to the principals room
Cleison hears someone calling him. He did not know who it was. He looked and saw a woman wearing a t-shirt with the words : Become Claudemilson. 
She said:
-Go to the Principals room!!!!
He remembered that  in his time he had a principal named George that was cool.
He did not understand anything, only followed the woman. In the principas room, she said
-You will have to listen to a rap and a funk of the dictatorship of Claudemilson and eat raw noodles!!!
Out of nowhere started a beat: Become Claudemilson
Wile Claudemilson was not seeing, Claison escaped.
When he ran away, he got into his car and went around desperately, but a traffic policeman stopped him . In this meanwhile, Claudemilson had time to reach him.Claudemilson began to shout with Cleison and in the meantime a fiscal that passed near there decided to enter the school .He saw that Claudemilson tortured the children, and she was arrested.
""" 
        _vai.vai = Texto(historia, '', texto, foi=redir).vai
        historia.vai()
    def go_principalsroom():
        _go_principalsroom()
        
    def __go_principalsroom():
        from naomi.main import secretaria
        secretaria().secretaria.vai()
        
    principalsroom_ = _sala = Sala(Principals_room_n,Principals_room_o,Principals_room_l,Principals_room_s, "principal")
    from naomi.main import Elemento
    _sala.sul.meio.vai = go_principalsroom
    caixa = Elemento(caixa_mae, tit = "pipe", drag=True,
        x = 480, y = 140, w = 180, h = 290, drop="router rack",
       cena=_sala.norte, texto="Please help me, fix my name.")
    clip  = Elemento(clips_, tit = "power plug", drag=True,
        x = 260, y = 410, w = 80, h = 100, drop="clips",
        cena=_sala.leste, texto="Please help me, fix my name.")

    pipes = Elemento(pipe_, tit = "router rack", drop="pipe",
        x = 500, y = 5, w = 100, h = 120,
        cena=_sala.norte, texto="Please help me, fix my name.")
    power = Elemento(power_plug, tit = "locker", drag=True,
        x = 510, y = 360, w = 100, h = 90, drop="power plug",
       cena=_sala.leste, texto="Please help me, fix my name.")
    doorl = Elemento(door_lock, tit = "keyboard", drag=True,
        x = 440, y = 380, w = 80, h = 100, drop="locker",
        cena=_sala.sul, texto="Please help me, fix my name.")
    keyboard_ = Elemento(keyboard, tit = "clips", drag=True,
        x = 300, y = 300, w = 100, h = 70, drop="keyboard",
        cena=_sala.leste, texto="Please help me, fix my name.")

    return _sala


if __name__ == "__main__": 
    INVENTARIO.inicia()
    principalsroom().norte.vai()