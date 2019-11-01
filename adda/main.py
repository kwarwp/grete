# grete.adda.main.py
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv 
FLORESTA="https://static.wixstatic.com/media/915324_a7aefd445f9c4b9d8703509a351c0258.jpg/v1/fill/w_637,h_311,al_c,q_80,usm_0.66_1.00_0.01/915324_a7aefd445f9c4b9d8703509a351c0258.webp"
ELEMENTO="http://www.dlf.pt/png/big/1/11494_soldado-png.png"
class wlg():
    floresta= Cena(img=FLORESTA)
    elemento= Elemento(img=ELEMENTO)
    elemento.entra(floresta)
    floresta.vai()
wlg()