import atheris

with atheris.instrument_imports():
  import P1.Task1
  import sys

def TestOneInput(data):
  P1.Task1.parse(data)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
