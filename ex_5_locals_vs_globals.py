"""
Variabes created outside  a functions are globals
variable created inside a functions are locals

A variable created outside of a function is global and can be used by anyone:

"""


x = 300


def myfunc():
    print(x)


myfunc()

print(x)


# The function will print the local x, and then the code will print the global x:

y = 300


def myfunc2():
    y = 200
    print(y)


myfunc2()

print(y)