
{'date': 'Mon Jun 11 2018 14:09:10.95 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 2
  Principals room 1 = "https://imgur.com/a/NwXyGcM?s=wa"
              ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jun 11 2018 14:54:40.697 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 6
    objects
NameError: name 'objects' is not defined
'''},