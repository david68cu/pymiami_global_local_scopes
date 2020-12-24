"""

The content of locals and globals will depend on where you call them.
Below example will show that the content of globals() will be different

So in 8 and 30 globals() = locals()
But in 18 , globals() != locals()  because local will be only {'x': 300}

"""

print(globals() == locals())


def myfunc():
    x = 300
    print(x)
    print("Locals inside myfunc() =", locals())  # => {'x': 300}
    print("Globals inside myfunc() =", globals())
    print(globals() == locals())


# The content of locals() and globals(0 will depend on where you call them

myfunc()


if __name__ == "__main__":
    print(globals() == locals())
