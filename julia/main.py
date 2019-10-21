# grete.julia.main.py    
from _spy.vitollino.main import Cena
QUARTO="https://i.imgur.com/awgqLtb.jpg"
ESCOLA="https://i.imgur.com/DtEkan7.jpg"
class Jogo:
	def inicia (self):
         primeira_Cena=Cena(QUARTO)
         segunda_Cena=Cena(ESCOLA)
         primeira_Cena.direita=segunda_Cena
         primeira_Cena.vai()
jogo=Jogo()
jogo.inicia()
        