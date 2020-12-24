"""

The content of locals and globals will depend on where you call them.
Below example will show that the content of globals() will be the same to locals()
in all the below calls in line 7. 19 amd 26

"""

print(globals() == locals())


def myfunc():
    x = 300
    print(x)


# The content of locals() and globals(0 will depend on where you call them

print("Locals =", locals())
print("Globals =", globals())
print(globals() == locals())
myfunc()


if __name__ == "__main__":
    print(globals() == locals())


# OUTPUT
"""
True
Locals = {
  '__name__': '__main__',
  '__doc__': '\n\nThe content of locals and globals will depend on where you call them.\nBelow example will show that the content of globals() will be the same to locals()\nin all the below calls in line 7. 19 amd 26\n\n',
  '__package__': None,
  '__loader__': <_frozen_importlib_external.SourceFileLoaderobjectat0x7f8e42e516d0>, 
  '__spec__': None,
  '__annotations__': {},
  '__builtins__': <module 'builtins'(built-in)>,
  '__file__': 'ex1_local.py',
  '__cached__': None,
  'myfunc': <function myfunc at 0x7f8e440f8820>,
}
Globals = {
  '__name__': '__main__',
  '__doc__': '\n\nThe content of locals and globals will depend on where you call them.\nBelow example will show that the content of globals() will be the same to locals()\nin all the below calls in line 7. 19 amd 26\n\n',
  '__package__': None,
  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8e42e516d0>,
  '__spec__': None,
  '__annotations__': {},
  '__builtins__': <module 'builtins' (built-in)>,
  '__file__': 'ex1_local.py',
  '__cached__': None,
  'myfunc': <function myfunc at 0x7f8e440f8820>
}
True
300
True
"""


