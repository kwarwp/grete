
{'date': 'Mon Nov 11 2024 13:16:54.90 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 1
  from _spy.vitollino.main  import Cena, 
                                        ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Mon Nov 11 2024 13:19:30.251 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 1
  from _spy.vitollino.main  import Cena, 
                                        ^
SyntaxError: trailing comma not allowed without surrounding parentheses
'''},
{'date': 'Mon Nov 11 2024 13:32:27.470 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 6
    FlorestaCena = Cena(Floresta,y=50,x=50)
  module _spy.vitollino.main line 1096
    Cena.c(**kwargs)
  module _spy.vitollino.main line 1139
    imagem, kwargs = (imagem, {}) if isinstance(imagem, str) \
AttributeError: 'int' object has no attribute '__getitem__'
'''},