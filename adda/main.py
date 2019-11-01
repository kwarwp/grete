# grete.adda.main.py
from _spy.vitollino.main import Cena, Elemento
from _spy.vitollino.main import INVENTARIO as inv
FLORENCA="https://aefirenze.it/images/Via_dei_calzaioli.jpg"
EZIO="https://www.freepngimg.com/thumb/assassins_creed/20532-7-ezio-auditore-file.png"
class davi():
    florenca=Cena(img=FLORENCA)
    ezio=Elemento(img=EZIO)
    ezio.entra(florenca)
    florenca.vai()
davi()    