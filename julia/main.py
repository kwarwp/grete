# grete.julia.main.py
from _spy.vitollino.main import STYLE, INVENTARIO, Sala, Texto, Cena, Elemento

jogadordefutebol = "https://png.pngtree.com/element_origin_min_pic/16/09/10/1357d39a3fa4fe0.jpg"
campodefutebol  = "https://papel.deparede.com.br/wp-content/uploads/2011/05/campo-de-futebol-330x247.jpg"
def Historia():
	cenaCampo = Cena(img = "https://papel.deparede.com.br/wp-content/uploads/2011/05/campo-de-futebol-330x247.jpg")
	cenaCampo.vai()
	jogador_defutebol = Elemento(img = "https://png.pngtree.com/element_origin_min_pic/16/09/10/1357d39a3fa4fe0.jpg", tit = "Jogador", style = dict (top = 50, left = 50 , height = 30, width = 40 ))
	jogador_defutebol.entra(cenaCampo)
	txtfala = Texto(cenaCampo, "Gostaria de jogar futebol aqui, se possivel.")
	jogador_defutebol.vai = txtfala.vai
Historia()
    
