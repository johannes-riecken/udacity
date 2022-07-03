import atheris

with atheris.instrument_imports():
  import P1.Task1
  import sys

def TestOneInput(data):
  cap = 0 if len(data) == 0 else data[0] % 10
  cache = P1.Task1.LRUCache(cap)
  sets = 0 if len(data[1:]) == 0 else data[1] % 10
  for i in range(sets):
    cache.set(i, i)
  gets = 0 if len(data[2:]) == 0 else data[2] % 10
  for i in range(gets):
    cache.get(i)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
