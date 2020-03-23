"""
The content of locals and globals will depend on where you call them.
Below example will show that the content of globals() will be the same to locals()
in all the below calls in line 12 and 31

Also locals() will autoupdate each time we created new local scope variables in function or classes
See how locals  changes in lines 176 , 18 and 27

"""
print("Locals =", locals())
print("Globals =", globals())
print(globals() == locals())


def myfunc():
    print("locals 1:", locals())   # locals() is empty
    x = 1
    print("locals 2:", locals())   # {'x': 1}
    print(globals() == locals())   # False


myfunc()


class Test:
    def __init__(self):
        print("locals inside Test:", locals())  # {'self': <__main__.Test object at 0x10338ccd0>}


if __name__ == "__main__":
    print(globals() == locals())
    test = Test()