
{'date': 'Mon May 28 2018 14:16:15.76 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 175
  mic = Elemento(MIC, tit = "sweep pan", drag=False, drop="microscope"
                                                                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 28 2018 14:29:11.156 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 195
    geografia()
  module <module> line 177
    mic = Elemento(MIC, tit = "sweep pan", drag=False, drop="microscope",
  module <module> line 20
    self.img, self.tit = img, tit
  module <module> line 82
    self.elt.title = texto
AttributeError: 'Elemento' object has no attribute 'elt'
'''},
{'date': 'Mon May 28 2018 14:52:40.936 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 70
  _texto = self.texto self.tit == self.title else CORRETO.format(self.tit)
                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jun 11 2018 11:18:52.73 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 63
  self._do_foi()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Mon Jun 11 2018 12:51:55.842 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 185
    GEO = geografia()
  module <module> line 178
    pan = Elemento(PAN, tit="earth globe", drag=False, drop="sweep pan",
NameError: name 'panstyle' is not defined
'''},
{'date': 'Mon Jun 11 2018 12:52:45.252 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 193
    GEO.oeste.vai()
AttributeError: 'NoneType' object has no attribute 'oeste'
'''},
{'date': 'Tue Jul 17 2018 02:07:44.834 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 196
    geografia().sul.vai()
  module <module> line 185
    _sala.sul.meio = Cena(vai=_go_gymnasiun)
NameError: name '_go_gymnasiun' is not defined
'''},