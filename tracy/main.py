# grete.tracy.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
CASTELO="https://http2.mlstatic.com/painel-lona-fosca-castelo-cinderela-2-x-150envio-48hs-D_NQ_NP_405405-MLB25019727073_082016-F.jpg"
PRINCESA="https://i.pinimg.com/236x/c9/72/7f/c9727fb053357c5f764297d170d54231--disney-princess-cupcakes-disney-princess-ariel.jpg" 
CASAL="https://1.bp.blogspot.com/-Kpu0Abwjqe0/TyS1cAygHGI/AAAAAAAADhk/eWsZn-I6vXs/s1600/Ariel-and-Eric-disney-couples-500-500.jpg" 
UNDER_THE_SEA=""
def historia_com_castelo():
    cena_com_castelo = Cena(img=CASTELO)
    princesa = Elemento(img=PRINCESA, tit="bom dia a todos meu nome é Ariel ", style=dict(width=100, height=150))
    princesa.entra(cena_com_castelo)
    fala_ariel = Texto(cena_com_castelo,"pode não parecer mas eu guardo vários segredos como que eu sou uma sereia!")
    princesa.vai = fala_ariel.vai
    cena_com_castelo.vai()
    
    
historia_com_castelo()