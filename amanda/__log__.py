
{'date': 'Mon Jun 11 2018 11:03:26.29 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 38
  x = 30, y = 500, w = 100, h = 120, drop="volcano",
                                         ^
SyntaxError: keyword argument repeated
'''},
{'date': 'Mon Jun 11 2018 13:09:43.283 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 54
    trigonometria().norte.vai()
  module <module> line 36
    _sala.sul.meio.vai = vai_geo
AttributeError: 'tuple' object has no attribute 'sul'
'''},