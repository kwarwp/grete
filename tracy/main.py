# grete.tracy.main.py
from _spy.vittolino.main import Cena, Elemento, Texto
CASTELO="https://http2.mlstatic.com/painel-lona-fosca-castelo-cinderela-2-x-150envio-48hs-D_NQ_NP_405405-MLB25019727073_082016-F.jpg"
PRINCESA="https://i.pinimg.com/236x/c9/72/7f/c9727fb053357c5f764297d170d54231--disney-princess-cupcakes-disney-princess-ariel.jpg" 
 
def historia_com_castelo():
    cena_com_castelo = Cena(img=CASTELO)
    princesa = Elemento(img=PRINCESA)
    princesa.entra(cena_com_castelo)
    cena_com_castelo.vai()
    
    
historia_com_castelo