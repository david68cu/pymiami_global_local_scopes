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
